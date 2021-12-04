import pandas as pd
def weekday_number(date):
  ''' Returning the weekday number of a date, e.g., 0 for Mondays.

  Parameters
  ----------
  date: datetime
    A datetime for which to find the weekday number.

  Returns
  -------
  weekday_number: int
    The weekday number of the date.
  '''

  weekday_number = date.weekday()
  return weekday_number


def weekday(date):
  ''' Returning the name of the weekday for a date.

  Parameters
  ----------
  date: datetime
    A datetime for which to find the weekday.

  Returns
  -------
  weekday: str
    The weekday of the date.
  '''
  
  day_number = date.weekday()
  week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  weekday = week_days[day_number]
  return weekday

def week(date):
  ''' Returning the week number of a date.

  Parameters
  ----------
  date: datetime
    A datetime for which to find the weekday.

  Returns
  -------
  week_number: int
    The week number of the date.
  '''

  week_number = date.week()
  return week_number

def month(date):
  ''' Returning the month name of date.

  Parameters
  ----------
  date: datetime
    A date for which to find the month name.

  Returns
  -------
  name_month: str
    The name of the month.
  '''

  name_month = date.month_name()
  return name_month


def add_time(chunk):
  ''' Adding columns for weekday, weekday number and month name to a chunk.

  Parameters
  ----------
  chunk: dataframe
    The chunk for which to add date information.

  Returns
  -------
  chunk: dataframe
    The chunk with date information.
  '''

  chunk['weekday'] = chunk['date'].apply(lambda x: weekday(x)) 
  chunk['Month'] =  chunk['date'].apply(lambda x: month(x))
  chunk['date_short'] = pd.to_datetime(chunk['date']).dt.date
  return chunk

def add_dict(key, dictionary):
  ''' Incrementing the value of a key in a dictionary.
  
  Parameters
  ----------
  key: object
    The key for which to increment the value.
  
  dictionary: dict
    A dictionary in which we are incrementing the value of the key, or adding the key if not already present.

  Returns
  -------
  dictionary: dict
    The given dictionary after incrementing the value.
  '''
  
  if key in dictionary:
    dictionary[key] += 1
  else:
    dictionary[key] = 1
  return dictionary


def to_dict(dictionary, chunk_column):
  ''' Making a column of a dataframe into a dictionary, e.g., making a dictionary where weekdays are keys,
  and the values are the number of occurences of the key in the key.
  
  Parameters
  ----------
  dictionary: dict
    An initalized dictionary, either containing some preset keys or empty.
  
  chunk_column: series
    A series containing a column of a dataframe.

  Returns
  -------
  dictionary: dict
    A dictionary containing the desired values and keys as descripted.
  '''

  chunk_column.apply(lambda x: add_dict(x, dictionary))
  return dictionary

def find_media(url, medias_list):
  ''' Returning the media outlet where the quote is found, 
  but only if the outlet is present in medias_list.
  
  Parameters
  ----------
  url: array
    An entry in the column 'urls' of the Quotebank dataset, where the first value is the first source where the quote was found.
  
  medias_list: array
    An array containing some chosen media outlets, e.g., 'nytimes'.
  
  Returns
  -------
  media: str
    The first entry in url if its present in medias_list.
  '''

  for string in medias_list:
    url_string = str(url[0])
    if string in url_string:
      media = string
      return media


def get_media(chunk, medias_list):
  ''' Adding column with the media outlet where the quote is first found, 
  but only if the outlet is present in medias_list.
  
  Parameters
  ----------
  chunk: dataframe  
    A chunk of the Quotebank dataset.

  medias_list: array
    An array containing some chosen media outlets represented as strings, e.g., 'nytimes'.

  Returns
  -------
  chunk: dataframe
    The given chunk of the dataset, now containing a column 'media_outlet' 
    keeping the media where the quote was first found.
  '''

  chunk['media_outlet'] = chunk['urls'].apply(lambda x: find_media(x, medias_list))
  return chunk