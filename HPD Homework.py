# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas

# <codecell>

from urllib import urlopen
from pandas import read_csv, set_option

# <codecell>

# HPD is a dataset of all the New York City 311 complaints related to the Department of Housing Preservation and Development 

HPD = read_csv("HPD2013.csv")

# <codecell>

help(read_csv)

# <codecell>

#let's look at the data

HPD.head()

# <codecell>

print "HPD has", HPD.shape[0], "rows and",HPD.shape[1],"columns"

# <codecell>

# Initially, I was hoping NYCHA buildings would be included, but it seems to be only residential

HPD["Location Type"].value_counts()

# <codecell>

#let's have a look at the distribution of complaints ber borough. Unsurprisingly, Brooklyn has the most complaints. 

HPD["Borough"].value_counts().plot(kind="barh")

# <codecell>

# Let's look at the type of complaints. Heating is the most common one by far with 201781 requests. Nobody requests HPD Literature. 

HPD["Complaint Type"].value_counts()

# <codecell>

# Let's see how the complaints are distributed per borough. The Bronx has the most heat related complaints, 
#even though it's not the most populous borough and Brooklyn has more complaints overall. 
# It's a story!

from pandas import crosstab
complaints = crosstab(HPD["Borough"],HPD["Complaint Type"])
complaints

# <codecell>

#Here it tried out some mapping stuff, which didn't work. But let's keep the code for later. 

# from urllib import urlretrieve
# url = "http://www.nyc.gov/html/dcp/download/bytes/nybb_13a.zip"
# urlretrieve(url,"nybb_13a.zip")

# <codecell>

# %%script bash
# unzip nybb_13a.zip

# <codecell>

# from geopandas import GeoDataFrame

# boros = GeoDataFrame.from_file('nybb_13a/nybb.shp')
# boros

# <codecell>

# boros["fake"] = [100,10,5,2,100]

# figure(figsize=[10,10])
# boros.plot("Shape_Area",colormap="Blues")
# show()

# <codecell>

#from pandas import merge
#help(merge)

# <codecell>

#merge(complaints, boros, left_on="Borough", right_on="BoroName")

# <codecell>

#HPD["Complaint Type"].is("HEATING")

# <codecell>

#Let's look at our original dataset again

HPD.describe()

# <codecell>

# Let's subset the heating related complaints

HEAT = HPD[HPD["Complaint Type"]=="HEATING"]

# <codecell>

#Let's have look!
HEAT

# <codecell>

#Let's see where the most complaints are located. Also a way to verify nothing got lost along the way. Still 67306 in the Bronx

HEAT["Borough"].value_counts()

# <codecell>

#Let's look at the column names

HEAT.columns

# <codecell>

# I would like to look how long it took for the complaint to be settled in different parts of the city. Does it take longer in the Bronx?
# Let's subset the column containing information about when the complaint was filed

created_date = HEAT["Created Date"]

# <codecell>

#Let's have a look. 

created_date.head()

# <codecell>

#Let's convert it to a workable format

from pandas import to_datetime

# <codecell>

created_dates = to_datetime(created_date,format='%m/%d/%Y %I:%M:%S %p',coerce=True)
created_dates.head()

# <codecell>

#Let's do the same for the date at which the complaints were closed

closed_date = HEAT["Closed Date"]
closed_dates = to_datetime(closed_date,format='%m/%d/%Y %I:%M:%S %p',coerce=True)
closed_dates.head()

# <codecell>

#Let's convert it to day of the year 

doy_created = created_dates.apply(lambda t: t.dayofyear)

# <codecell>

#Let's have a look at the distribution.It would be interesting to plot this this against median temperatures. 
# It looks like the 24th and the 329th day of the year were particularly bad. 
# Indeed, the fourth week of January was particularly cold, with temperatures in the low 20s. 
# The second spike coincides with the last week of November, which had temperatures in the low 30s. 

doy_created.value_counts().sort_index().plot(figsize=[20,10])
vlines(24,0,6000)
vlines(329,0,6000)
show()

# <codecell>

# Let's do the same for the close dates

doy_closed = closed_dates.apply(lambda t: t.dayofyear)

# <codecell>

doy_closed.head()

# <codecell>

type(doy_created)
    

# <codecell>

doy_created[2]

# <codecell>

doy_created[23]

# <codecell>

#Let's look at the number of days it took for cases to be closed

for d in doy_created:
    length.append(int(doy_closed[d])-int(doy_created))

# <codecell>


# <codecell>


