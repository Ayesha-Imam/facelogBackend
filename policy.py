# from config import Resource, reqparse

# TimeInterval_parser = reqparse.RequestParser()
# TimeInterval_parser.add_argument("attendance_start_time", type= str, help = "time is required", required= True)
# TimeInterval_parser.add_argument("attendance_end_time", type= str, help = "time is required", required= True)
# TimeInterval_parser.add_argument("present_time", type= str, help = "time is required", required= True)
# TimeInterval_parser.add_argument("late_time", type= str, help = "time is required", required= True)
# TimeInterval_parser.add_argument("half_day_time", type= str, help = "time is required", required= True)


# class TimeInterval(Resource):
#     def post(self):
#         args = TimeInterval_parser.parse_args()
#         attendance_start_time = args["attendance_start_time"]
#         attendance_end_time = args["attendance_end_time"]
#         present_time = args["present_time"]
#         late_time = args["late_time"]
#         half_day_time = args["half_day_time"]

#         # Check if all required data is present
#         if all(arg is not None for arg in args.values()):
#             # Data received successfully, you can use the variables as needed
#             return {
#                 "data": "Data received successfully",
#                 "attendance_start_time": attendance_start_time,
#                 "attendance_end_time": attendance_end_time,
#                 "present_time": present_time,
#                 "late_time": late_time,
#                 "half_day_time": half_day_time
#             }, 201
#         else:
#             # Data not received as expected
#             return {"error": "Failed to receive data"}, 500

# class Days(Resource):
    

# class SalaryDeduction(Resource):
        


from config import Resource, reqparse
from datetime import datetime

class TimeInterval(Resource):
    # Store time values as datetime.time objects
    attendance_start_time = None
    attendance_end_time = None
    present_time = None
    late_time = None
    half_day_time = None

    TimeInterval_parser = reqparse.RequestParser()
    TimeInterval_parser.add_argument("attendance_start_time", type= str, help = "time is required", required= True)
    TimeInterval_parser.add_argument("attendance_end_time", type= str, help = "time is required", required= True)
    TimeInterval_parser.add_argument("present_time", type= str, help = "time is required", required= True)
    TimeInterval_parser.add_argument("late_time", type= str, help = "time is required", required= True)
    TimeInterval_parser.add_argument("half_day_time", type= str, help = "time is required", required= True)

    @classmethod
    def set_values(cls, args):
        cls.attendance_start_time = args.get("attendance_start_time")
        cls.attendance_end_time = args.get("attendance_end_time")
        cls.present_time = args.get("present_time")
        cls.late_time = args.get("late_time")
        cls.half_day_time = args.get("half_day_time")


    @classmethod
    def get_values(cls):
        return {
            "attendance_start_time": cls.attendance_start_time,
            "attendance_end_time": cls.attendance_end_time,
            "present_time": cls.present_time,
            "late_time": cls.late_time,
            "half_day_time": cls.half_day_time
        }

    def post(self):
        args = self.TimeInterval_parser.parse_args()
        self.set_values(args)
        return {"message": "Time interval set successfully"}, 201

    def get(self):
        return self.get_values(), 200
    
    # @classmethod
    # def set_values(cls, args):
    #     cls.attendance_start_time = datetime.strptime(args.get("attendance_start_time"), "%H:%M:%S").time()
    #     cls.attendance_end_time = datetime.strptime(args.get("attendance_end_time"), "%H:%M:%S").time()
    #     cls.present_time = datetime.strptime(args.get("present_time"), "%H:%M:%S").time()
    #     cls.late_time = datetime.strptime(args.get("late_time"), "%H:%M:%S").time()
    #     cls.half_day_time = datetime.strptime(args.get("half_day_time"), "%H:%M:%S").time()