
def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cats.append({"id": cat_id, "name": name, "age": age})

        return cats

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

path = "2/cats_info_file.txt"
cats_info = get_cats_info(path)
print(cats_info)