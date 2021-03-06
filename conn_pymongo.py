from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['hi_soi']

# print(db.collection_names(include_system_collections=False))
# pprint.pprint(db.startup_log.find_one())


def insert_correct_result(video_info, face_move_cnt):
    collection = db['correction_result']

    result = {"user_id": video_info["userId"],
              "video_save_name": video_info["videoSaveName"],
              "face_move_cnt": face_move_cnt,
              "cnt_per_5sec": video_info["cnt_per_5sec"],
              "date": datetime.datetime.now()}

    collection.insert_one(result)
    print("[SUCCESS] Inserted a correction result into MongoDB successfully.")


def get_video_info(video_no):
    collection = db['video_info']
    return collection.find_one({'videoNo': str(video_no)})


# def get_video_info(video_save_name):
#     collection = db['video_info']
#     return collection.find_one({'videoSaveName': video_save_name})


def update_correct_result(video_info):
    print(video_info)
    collection = db['video_info']
    collection.update_one({'videoNo': video_info['videoNo']},
                          {'$set': {"total_video_time": video_info['total_video_time'],
                                    "face_move_cnt": video_info['face_move_cnt'],
                                    "move_direction": video_info["move_direction"],
                                    "miss_location": video_info['miss_location'],
                                    "miss_section": video_info['miss_section'],
                                    "face_move_cnt_per_5sec": video_info["face_move_cnt_per_5sec"],
                                    "blink_cnt": video_info["blink_cnt"],
                                    "eye_blink_cnt_per_5sec": video_info["eye_blink_cnt_per_5sec"],
                                    "date": datetime.datetime.now()}})

    print("[SUCCESS] Inserted a correction result into MongoDB successfully.")


def update_swk_result(video_info):  # swk : Shoulder, wrist, knee
    collection = db['video_info']
    collection.update_one({'videoNo': video_info['videoNo']},
                          {'$set': {"shoulder_move_cnt": video_info["shoulder_move_cnt"],
                                    "wrist_move_cnt": video_info["wrist_move_cnt"],
                                    "knee_move_cnt": video_info["knee_move_cnt"],
                                    "s_move_direction": video_info["s_move_direction"],
                                    "w_move_direction": video_info["w_move_direction"],
                                    "k_move_direction": video_info["k_move_direction"],
                                    "s_move_cnt_per_5sec": video_info["s_move_cnt_per_5sec"],
                                    "w_move_cnt_per_5sec": video_info["w_move_cnt_per_5sec"],
                                    "k_move_cnt_per_5sec": video_info["k_move_cnt_per_5sec"]}})

    print("[SUCCESS] Inserted shoulder, wrist and knee result into MongoDB successfully.")


def update_grade_and_time(video_info):
    collection = db['video_info']
    collection.update_one({'videoNo': video_info['videoNo']},
                          {'$set': {"total_grade": video_info['total_grade'],
                                    "processing_time": video_info['processing_time']}})

    print("[SUCCESS] Inserted the total grade & processing_time into MongoDB successfully.")