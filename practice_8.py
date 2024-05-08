from datetime import datetime
import logging

logging.basicConfig(
    filename="logs_2.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def calculate_time_in_pool(start, end):
    try:
        start_time = datetime.strptime(start, "%d/%m/%Y %H:%M:%S")
        end_time = datetime.strptime(end, "%d/%m/%Y %H:%M:%S")
        time_difference = end_time - start_time
        time_in_minutes = time_difference.total_seconds() / 60
        rounded_time = round(time_in_minutes, 0)
        return rounded_time
    except Exception as e:
        logging.debug(f"Ошибка при обработке времени: {str(e)}")
        return None


def process_control_system_file(filename):
    athletes = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) != 4:
                logging.debug(f"mistake in str: {line.strip()}")
                continue

            timestamp, athlete_id, location, action = parts
            if action == "In":
                athletes[(athlete_id, location)] = timestamp
            elif action == "Out":
                if (athlete_id, location) in athletes:
                    start_time = athletes.pop((athlete_id, location))
                    time_in_pool = calculate_time_in_pool(start_time, timestamp)
                    if time_in_pool is not None:
                        print(
                            f"Атлет {athlete_id} провёл в {location}: {time_in_pool} мин."
                        )
                else:
                    logging.debug(
                        f"Не зафиксировано время входа атлета {athlete_id} в {location}"
                    )

    for athlete_location, start_time in athletes.items():
        athlete_id, location = athlete_location
        logging.debug(
            f"Не зафиксировано время выхода атлета {athlete_id} из {location}"
        )


process_control_system_file("athlete_data")
