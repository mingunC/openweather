from google.cloud import bigquery

def query_weather_table(project_id: str, dataset_id: str, table_id: str):
    client = bigquery.Client(project=project_id)
    table = f"`{project_id}.{dataset_id}.{table_id}`"

    sql = f"""
        SELECT
          DATE(timestamp) AS date,
          AVG(temperature_celsius) AS avg_temp_c,
          COUNT(*) AS record_count
        FROM {table}
        GROUP BY date
        ORDER BY date DESC
        LIMIT 7
    """

    job = client.query(sql)
    print("=== 최근 7일간 일별 평균 기온 ===")
    for row in job:
        print(f"{row.date}: {row.avg_temp_c:.2f}°C over {row.record_count} records")

if __name__ == "__main__":
    PROJECT_ID = "future-cat-458304-j8"
    DATASET_ID = "weather_data"
    TABLE_ID = "weather_20250429"

    query_weather_table(PROJECT_ID, DATASET_ID, TABLE_ID)