import datetime

def add_days(date_str, format_str, minutes):
    dt = datetime.datetime.strptime(date_str, format_str)
    return dt + datetime.timedelta(minutes)

class FilterModule(object):
  def filters(self):
      return {
          'add_days': add_days,
      }
