import os
import datetime
import remoclient
import spreadsheet


def run(*args, **kwags):
    gs = spreadsheet.SpreadSheet()
    gs.open_sheet(filename=os.environ['SHEET_NAME'])
    last_line = gs.get_col_length()
    if last_line == 0:
        header = [
            'timestamp',
            'timestamp_unix',
            'temperature',
            'temperature_created_at',
            'humidity',
            'humidity_created_at',
            'illumination',
            'illumination_created_at',
            'motion',
            'motion_created_at'
        ]
        gs.update_column(1, header)
        last_line += 1

    now = datetime.datetime.now(datetime.timezone.utc)
    client = remoclient.NatureRemoClient()
    events = client.get_newest_events()
    now_iso = now.isoformat()

    values = [
        now_iso,
        int(now.timestamp()),
        events['te']['val'],
        events['te']['created_at'],
        events['hu']['val'],
        events['hu']['created_at'],
        events['il']['val'],
        events['il']['created_at'],
        events['mo']['val'],
        events['mo']['created_at']
    ]

    if [str(v) for v in values[2:]] != gs.get_latest_row()[2:]:
        print('update')
        gs.update_column(last_line + 1, values)
    else:
        print('no update')

    print('done!')


if __name__ == "__main__":
    run()
