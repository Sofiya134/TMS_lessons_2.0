import json
def write_json_file():
    with open("json.json", "w", encoding='utf-8') as file:
        my_dict = {"name": "Софья",
                   "animal": "Выдра",
                   "age": 80}
        json.dump(
            my_dict,
            file,
            sort_keys=False,
            ensure_ascii=False,
            indent=4,
        )
write_json_file()

def read_jsonfile():
    with open("json.json", encoding="utf-8") as file:
        json_contents = json.load(file)
    return (json_contents)

task_list = read_jsonfile()
task_list['movie']= 'Cloud Atlas'

read_jsonfile()

def write_jsonfile():
    with open("json.json", "w", encoding="utf-8") as file:
        json.dump(
            task_list,
            file,
            ensure_ascii=False,
            indent=4,
        )

write_jsonfile()