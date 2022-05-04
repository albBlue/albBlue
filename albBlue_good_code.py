{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "46a2629d-6bdb-4e79-b9bd-2fc196226a67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+++ libraries loaded!\n"
     ]
    }
   ],
   "source": [
    "# LIBRARIES \n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "from os import path\n",
    "import xlsxwriter\n",
    "from pathlib import Path\n",
    "import csv\n",
    "import sys\n",
    "import altair as alt\n",
    "from datetime import date\n",
    "from datetime import datetime\n",
    "#import matplotlib.pyplot as plt\n",
    "#import pandas_profiling\n",
    "print(\"+++ libraries loaded!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "33686935-364f-40fd-9cfe-4c4317af5bf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2021-05-20\n",
      "SUFFIX date and time = 05202021_122238\n",
      "d1 = 20/05/2021\n",
      "d2 = May 20, 2021\n",
      "d3 = 05/20/21\n",
      "d4 = May-20-2021\n",
      "now = 2021-05-20 12:22:38.538679\n",
      "date and time = 20/05/2021 12:22:38\n",
      "date and time = 05202021_122238\n",
      "Current Time = 12:22:38\n",
      "Current Time = 12_22_38\n",
      "now = 12:22:38.539837\n",
      "type(now) = <class 'datetime.time'>\n"
     ]
    }
   ],
   "source": [
    "### ---- \n",
    "### DATE AND TIME VARIABLES\n",
    "### ---- \n",
    "today = date.today()\n",
    "print (today)\n",
    "\n",
    "from datetime import date\n",
    "from datetime import datetime\n",
    "\n",
    "today = date.today()\n",
    "\n",
    "# ddmmYY_HHMMSS\n",
    "\n",
    "now = datetime.now()\n",
    "dt_string = now.strftime(\"%m%d%Y_%H%M%S\")\n",
    "print(\"SUFFIX date and time =\", dt_string)\n",
    "\n",
    "# dd/mm/YY\n",
    "d1 = today.strftime(\"%d/%m/%Y\")\n",
    "print(\"d1 =\", d1)\n",
    "\n",
    "# Textual month, day and year\t\n",
    "d2 = today.strftime(\"%B %d, %Y\")\n",
    "print(\"d2 =\", d2)\n",
    "\n",
    "# mm/dd/y\n",
    "d3 = today.strftime(\"%m/%d/%y\")\n",
    "print(\"d3 =\", d3)\n",
    "\n",
    "# Month abbreviation, day and year\t\n",
    "d4 = today.strftime(\"%b-%d-%Y\")\n",
    "print(\"d4 =\", d4)\n",
    "\n",
    "# datetime object containing current date and time\n",
    "now = datetime.now()\n",
    "print(\"now =\", now)\n",
    "\n",
    "# dd/mm/YY H:M:S\n",
    "dt_string = now.strftime(\"%d/%m/%Y %H:%M:%S\")\n",
    "print(\"date and time =\", dt_string)\n",
    "\n",
    "# ddmmYY_HHMMSS\n",
    "dt_string = now.strftime(\"%m%d%Y_%H%M%S\")\n",
    "print(\"date and time =\", dt_string)\n",
    "\n",
    "\n",
    "current_time = now.strftime(\"%H:%M:%S\")\n",
    "print(\"Current Time =\", current_time)\n",
    "\n",
    "current_time = now.strftime(\"%H_%M_%S\")\n",
    "print(\"Current Time =\", current_time)\n",
    "\n",
    "\n",
    "now = datetime.now().time() # time object\n",
    "print(\"now =\", now)\n",
    "print(\"type(now) =\", type(now))\t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb102664-c625-4492-960f-fdc8a4595458",
   "metadata": {},
   "outputs": [],
   "source": [
    "## ------\n",
    "## FILES \n",
    "## ------\n",
    "home_dir = './'\n",
    "in_dir = os.path.join(home_dir, 'in_dir')\n",
    "out_dir = os.path.join(home_dir, 'out_dir')\n",
    "csv_files = [os.path.join(in_dir , f) for f in os.listdir(in_dir) if (\".csv\" in f and \"~\" not in f) ]\n",
    "print(csv_files)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20df94c7-6971-4487-a06e-600085fa7847",
   "metadata": {},
   "outputs": [],
   "source": [
    "# FILES Alternate \n",
    "# files = os.listdir(path)\n",
    "# for f in files:\n",
    "# \tprint(f)\n",
    "#   print(os.path.join(root, name))\n",
    "\n",
    "# directory = os.path.join(\"c:\\\\\",\"path\")\n",
    "# for root,dirs,files in os.walk(directory):\n",
    "#     for file in files:\n",
    "#        if file.endswith(\".csv\"):\n",
    "#            f=open(file, 'r')\n",
    "#            #  perform calculation\n",
    "#            f.close()\n",
    "\n",
    "# print(files)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43808146-74e1-429c-8284-5862da7e8762",
   "metadata": {},
   "outputs": [],
   "source": [
    "## --{\n",
    "## CREATE DF form CSV \n",
    "## --- \n",
    "# CONCATENATE many csv files in one df\n",
    "df_raw = pd.concat((pd.read_csv(f) for f in csv_files))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcf90d78-8e4a-4a1e-80cc-f9c64d1f7581",
   "metadata": {},
   "outputs": [],
   "source": [
    "## --- \n",
    "## SAVE DF into a CSV \n",
    "## --- \n",
    "out_file = \"out_file.csv\"\n",
    "now = datetime.now()\n",
    "pre_fix = now.strftime(\"%m%d%Y_%H%M%S_\")\n",
    "df_raw.to_csv(out_dir + '/' + pre_fix + out_file)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71e167db-aeac-4732-93bc-5c6f843b5d91",
   "metadata": {},
   "outputs": [],
   "source": [
    "## ---\n",
    "## DF ANALYSIS \n",
    "## ---\n",
    "df           # print the first 30 and last 30 rows\n",
    "type(df)     # DataFrame\n",
    "df.head()    # print the first 5 rows\n",
    "df.head(10)  # print the first 10 rows\n",
    "df.tail()    # print the last 5 rows\n",
    "df.index     # “the index” (aka “the labels”)\n",
    "df.columns   # column names (which is “an index”)\n",
    "df.dtypes    # data types of each column\n",
    "df.shape     # number of rows and columns\n",
    "# underlying numpy array — df are stored as numpy arrays for effeciencies.\n",
    "df.values\n",
    "df['Market Code'].value_counts()\n",
    "df['Market Code'].unique()\n",
    "\n",
    "\n",
    "del df_resp # Delete "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c82e0142-112d-4001-8af0-465f22bbe014",
   "metadata": {},
   "outputs": [],
   "source": [
    "### ----\n",
    "# DF COLUMN ANALYSIS\n",
    "### ----\n",
    "\n",
    "df[‘column_y’]         # select one column\n",
    "type(df[‘column_y’])   # determine datatype of column (e.g., Series)\n",
    "\n",
    "# summarize (describe) the DataFrame\n",
    "df.describe()          # describe all numeric columns\n",
    "df.describe(include=[‘object’])  # describe all object columns\n",
    "df.describe(include=’all’)      # describe all columns\n",
    "\n",
    "#filter df by one column, and print out values of another column\n",
    "#when using numeric values, no quotations\n",
    "df[df.column_y == “string_value”].column_z\n",
    "df[df.column_y == 20].column_z\n",
    "\n",
    "# display only the number of rows of the ‘df’ DataFrame\n",
    "df.shape[0]\n",
    "# display the 3 most frequent occurances of column in ‘df’\n",
    "df.column_y.value_counts()[0:3]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce1459dd-86f8-4e7a-b85f-177d894e8bc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "### --- \n",
    "### DF FILTER\n",
    "### ---- \n",
    "# boolean filtering: only show df with column_z < 20\n",
    "filter_bool = df.column_z < 20    # create a Series of booleans…\n",
    "df[filter_bool]                # …and use that Series to filter rows\n",
    "df[filter_bool].describe()     # describes a data frame filtered by filter_bool\n",
    "df[df.column_z < 20]           # or, combine into a single step\n",
    "df[df.column_z < 20].column_x  # select one column from the filtered results\n",
    "df[df[“column_z”] < 20].column_x     # alternate method\n",
    "# value_counts of resulting Series, can also use .mean(), etc. instead of .value_counts()\n",
    "df[df.column_z < 20].column_x.value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "609313cd-7e90-4731-ae0c-472030b3b074",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character '‘' (U+2018) (<ipython-input-1-fe055e46efca>, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-fe055e46efca>\"\u001b[0;36m, line \u001b[0;32m5\u001b[0m\n\u001b[0;31m    fooframe = pd.DataFrame({‘Size’:[‘Large’, ‘Medium’, ‘Small’, ‘Tiny’], 'Color':[1, 2, 3, 4]})\u001b[0m\n\u001b[0m                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid character '‘' (U+2018)\n"
     ]
    }
   ],
   "source": [
    "### --- \n",
    "### DF QUERY \n",
    "### ---- \n",
    "import pandas as pd\n",
    "fooframe = pd.DataFrame({‘Size’:[‘Large’, ‘Medium’, ‘Small’, ‘Tiny’], 'Color':[1, 2, 3, 4]})\n",
    " # classic way \n",
    "subframe = fooframe[fooframe['Size'] == 'Large']\n",
    "\n",
    "# query way \n",
    "subframe = fooframe.query(“Size == ‘Large’”)\n",
    "# with var in \n",
    "my_size = ‘Large’\n",
    "subframe = fooframe.query(“Size == @my_size”)\n",
    "# w/ col as a var \n",
    "col_n = ‘Size’\n",
    "my_size = ‘Large’\n",
    "subframe = fooframe.query(f”{col_n } == ‘{my_size}’”)\n",
    "# NOTE: Because you are building a string to query, you need the ‘’quotes around my_size \n",
    "# to indicate to .query() to expect a string to compare to.\n",
    "\n",
    "df.query('Size == \"Large\" and Color != \"1\" ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccbc978f-d7ee-4023-8d2b-b0df9a6677bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "### --- \n",
    "### DROP \n",
    "### --- \n",
    "\n",
    "df = df.drop(some labels)\n",
    "df = df.drop(df[<some boolean condition>].index)\n",
    "\n",
    "## Use dropna with parameter subset for specify column for check NaNs:\n",
    "# 1. Dropping columns\n",
    "# The drop function is used to drop columns and rows. We pass the labels of rows or columns to be dropped.\n",
    "df.drop(['RowNumber', 'CustomerId', 'Surname', 'CreditScore'], axis=1, inplace=True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1349e5b1-69fe-481d-8770-8f8a90f6a477",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5aa414e4-a767-43af-97be-f616f8ad4278",
   "metadata": {},
   "outputs": [],
   "source": [
    "## --- \n",
    "## APPLY an IF condition in Pandas DataFrame\n",
    "## https://datatofish.com/if-condition-in-pandas-dataframe/\n",
    "## --- \n",
    "### 1 \n",
    "### If the number is equal or lower than 4, then assign the value of ‘True’skus_resp_list\n",
    "### Otherwise, if the number is greater than 4, then assign the value of ‘False’\n",
    "df.loc[df['column name'] condition, 'new column name'] = 'value if condition is met'\n",
    "df.loc[df['set_of_numbers'] <= 4, 'equal_or_lower_than_4?'] = 'True' \n",
    "df.loc[df['set_of_numbers'] > 4, 'equal_or_lower_than_4?'] = 'False' \n",
    "\n",
    "### 2 (2) IF condition – set of numbers and lambda\n",
    "df['new column name'] = df['column name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')\n",
    "df['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(lambda x: 'True' if x <= 4 else 'False')\n",
    "\n",
    "### 3) IF condition – strings\n",
    "### If the name is equal to ‘Bill,’ then assign the value of ‘Match’\n",
    "### Otherwise, if the name is not ‘Bill,’ then assign the value of ‘Mismatch’\n",
    "df.loc[df['First_name'] == 'Bill', 'name_match'] = 'Match'  \n",
    "df.loc[df['First_name'] != 'Bill', 'name_match'] = 'Mismatch'  \n",
    "\n",
    "### 4) IF condition – strings and lambada \n",
    "df['name_match'] = df['First_name'].apply(lambda x: 'Match' if x == 'Bill' else 'Mismatch')\n",
    "\n",
    "### 5) IF condition with OR\n",
    "df.loc[(df['First_name'] == 'Bill') | (df['First_name'] == 'Emma'), 'name_match'] = 'Match'  \n",
    "df.loc[(df['First_name'] != 'Bill') & (df['First_name'] != 'Emma'), 'name_match'] = 'Mismatch'  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91d5de76-998c-4635-afdc-fd0a853eecc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "### ---\n",
    "### DF from Clipbard \n",
    "### ---\n",
    "df_raw = pd.read_clipboard()\n",
    "df_raw.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a08dc3c1-b2be-4184-a1ed-781528e4f2a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "### ---\n",
    "### F-string\n",
    "### ---\n",
    "a_var = \"a\"\n",
    "print(f\"{a_var = }\")\n",
    "\n",
    "float_variable = 3.141592653589793\n",
    "print(f\"{float_variable:.2f}\")\n",
    "\n",
    "\n",
    "money = 3_142_671.76\n",
    "print(f\"${money:,.2f}\")\n",
    "\n",
    "now = datetime.now()\n",
    "print (f\"{now:%d-%B-%Y}\")\n",
    "\n",
    "# Pad Output length of 20, and pad the rest with zeroes\n",
    "int_variable = 1_234_567\n",
    "print(f'{int_variable:020}')\n",
    "\n",
    "# Using repr() function\n",
    "print(f'{now!r}')\n",
    "# datetime.datetime(2021, 7, 5, 13, 2, 34, 672383)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6968467-5e8f-442f-8e1a-7fd793ceb1e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "## --- \n",
    "## 30 Examples to Master Pandas\n",
    "## https://towardsdatascience.com/30-examples-to-master-pandas-f8a2da751fa4\n",
    "## --- \n",
    "# create a DataFrame from a dictionary\n",
    "pd.DataFrame({‘column_x’: [‘value_x1’, ‘value_x2’, ‘value_x3’], ‘column_y’: [‘value_y1’, ‘value_y2’, ‘value_y3’]})\n",
    "# create a DataFrame from a list of lists\n",
    "pd.DataFrame([[‘value_x1’, ‘value_y1’], [‘value_x2’, ‘value_y2’], [‘value_x3’, ‘value_y3’]], columns=[‘column_x’, ‘column_y’])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76ebfb40-b4b1-4fc6-b48e-5dfcde11e826",
   "metadata": {},
   "source": [
    "30 Examples to Master Pandas\n",
    "https://towardsdatascience.com/30-examples-to-master-pandas-f8a2da751fa4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f27e923-4c1b-4209-8a22-b98255901c53",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c0d318ec-68b7-4c8b-95af-07d887b69d87",
   "metadata": {},
   "source": [
    "How to Create Pandas DataFrame in Python \n",
    "https://datatofish.com/create-pandas-dataframe/\n",
    "https://datatofish.com/python-tutorials/ "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9074876-5047-4900-900f-e388b0a8fc1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "## --- \n",
    "## How to Create Pandas DataFrame in Python \n",
    "## https://datatofish.com/create-pandas-dataframe/\n",
    "## --- \n",
    "# 1 - typing values in Python to create Pandas DataFrame\n",
    "data = {'First Column Name':  ['First value', 'Second value',...],\n",
    "        'Second Column Name': ['First value', 'Second value',...],\n",
    "         ....}\n",
    "df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])\n",
    "\n",
    "# OR  \n",
    "cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],\n",
    "        'Price': [22000,25000,27000,35000]}\n",
    "df = pd.DataFrame(cars, columns = ['Brand', 'Price'])\n",
    "\n",
    "#2 Method 2: importing values from an Excel file to create Pandas DataFrame\n",
    "data = pd.read_excel(r'Path where the Excel file is stored\\File name.xlsx') #for an earlier version of Excel use 'xls'\n",
    "df = pd.DataFrame(data, columns = ['First Column Name','Second Column Name',...])\n",
    "# ImportError: Install xlrd >= 1.0.0 for Excel support\n",
    "pip3 install xlrd\n",
    "\n",
    "\n",
    "# Get the maximum value from the DataFrame\n",
    "max1 = df['Price'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff1a39ce-2aba-402f-afb1-20b8bcdec20f",
   "metadata": {},
   "outputs": [],
   "source": [
    "### ADD multiple columns to pandas dataframe in one assignment\n",
    "\n",
    "# 1) Three assignments in one, using list unpacking:\n",
    "df['column_new_1'], df['column_new_2'], df['column_new_3'] = [np.nan, 'dogs', 3]\n",
    "\n",
    "#2) DataFrame conveniently expands a single row to match the index, so you can do this:\n",
    "df[['column_new_1', 'column_new_2', 'column_new_3']] = pd.DataFrame([[np.nan, 'dogs', 3]], index=df.index)\n",
    "\n",
    "#3) Make a temporary data frame with new columns, then combine with the original data frame later:\n",
    "df = pd.concat(\n",
    "    [\n",
    "        df,\n",
    "        pd.DataFrame(\n",
    "            [[np.nan, 'dogs', 3]], \n",
    "            index=df.index, \n",
    "            columns=['column_new_1', 'column_new_2', 'column_new_3']\n",
    "        )\n",
    "    ], axis=1\n",
    ")\n",
    "\n",
    "#4) Similar to the previous, but using join instead of concat (may be less efficient):\n",
    "df = df.join(pd.DataFrame(\n",
    "    [[np.nan, 'dogs', 3]], \n",
    "    index=df.index, \n",
    "    columns=['column_new_1', 'column_new_2', 'column_new_3']\n",
    "))\n",
    "\n",
    "#5) Using a dict is a more \"natural\" way to create the new data frame than the previous two, but the new columns will be sorted alphabetically (at least before Python 3.6 or 3.7):\n",
    "df = df.join(pd.DataFrame(\n",
    "    {\n",
    "        'column_new_1': np.nan,\n",
    "        'column_new_2': 'dogs',\n",
    "        'column_new_3': 3\n",
    "    }, index=df.index\n",
    "))\n",
    "\n",
    "#6) Use .assign() with multiple column arguments.\n",
    "#I like this variant on @zero's answer a lot, but like the previous one, the new columns will always be sorted alphabetically, at least with early versions of Python:\n",
    "df = df.assign(column_new_1=np.nan, column_new_2='dogs', column_new_3=3)\n",
    "\n",
    "#7) This is interesting (based on https://stackoverflow.com/a/44951376/3830997), but I don't know when it would be worth the trouble:\n",
    "new_cols = ['column_new_1', 'column_new_2', 'column_new_3']\n",
    "new_vals = [np.nan, 'dogs', 3]\n",
    "df = df.reindex(columns=df.columns.tolist() + new_cols)   # add empty cols\n",
    "df[new_cols] = new_vals  # multi-column assignment works for existing cols\n",
    "\n",
    "#8) In the end it's hard to beat three separate assignments:\n",
    "df['column_new_1'] = np.nan\n",
    "df['column_new_2'] = 'dogs'\n",
    "df['column_new_3'] = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d76eb320-f37f-42a4-b25c-eadec45f8ecf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "237ea56f-0d3f-4986-bc7a-346f92bb93c4",
   "metadata": {},
   "outputs": [],
   "source": [
    ">>> df = pd.DataFrame(columns=['lib', 'qty1', 'qty2'])\n",
    ">>> for i in range(5):\n",
    ">>>     df.loc[i] = ['name' + str(i)] + list(randint(10, size=2))\n",
    "\n",
    ">>> df\n",
    "     lib qty1 qty2\n",
    "0  name0    3    3\n",
    "1  name1    2    4\n",
    "2  name2    2    8\n",
    "3  name3    2    1\n",
    "4  name4    9    6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9159580-edec-4dd4-9db3-0ac4b7c53975",
   "metadata": {},
   "outputs": [],
   "source": [
    "def func(row):\n",
    "   if row['a'] == \"3\":\n",
    "        row2 = row.copy()\n",
    "        # make edits to row2\n",
    "        return pd.concat([row, row2], axis=1)\n",
    "   return row\n",
    "\n",
    "pd.concat([func(row) for _, row in df.iterrows()], ignore_index=True, axis=1).T\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ce1f3a6-6e4e-4841-b4f5-f341e6e18a8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def row_appends(x):\n",
    "    newrows = x.loc[x['a'].isin(['3', '4', '5'])].copy()\n",
    "    newrows.loc[x['a'] == '3', 'b'] = 10  # make conditional edit\n",
    "    newrows.loc[x['a'] == '4', 'b'] = 20  # make conditional edit\n",
    "    newrows.index = newrows.index + 0.5\n",
    "    return newrows\n",
    "\n",
    "res = pd.concat([df, df.pipe(row_appends)])\\\n",
    "        .sort_index().reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f79b8549-b47d-4fbd-96df-702ce4a996e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e96ed3b9-c9a9-4bbb-81bd-59fbb25c685a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# https://stackoverflow.com/questions/10715965/create-pandas-dataframe-by-appending-one-row-at-a-time \n",
    "### This is The Right Way™ to accumulate your data\n",
    "\n",
    "data = []\n",
    "for a, b, c in some_function_that_yields_data():\n",
    "    data.append([a, b, c])\n",
    "\n",
    "df = pd.DataFrame(data, columns=['A', 'B', 'C'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd62525e-d5ce-4389-97bf-8de8221006d7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7e371a9-f59a-4ecc-9aae-aea1e2fa133d",
   "metadata": {},
   "outputs": [],
   "source": [
    "market_store = {'CA':ca_test_store,'US':us_test_store}\n",
    "#df_bev['store'] = df_bev['Market Code'].map(market_store)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81b25dd0-7d8a-4ac8-9160-39e9129fa39e",
   "metadata": {},
   "outputs": [],
   "source": [
    "people = [\n",
    "{'name': \"Tom\", 'age': 10},\n",
    "{'name': \"Mark\", 'age': 5},\n",
    "{'name': \"Pam\", 'age': 7}\n",
    "]\n",
    "\n",
    "filter(lambda person: person['name'] == 'Pam', people)\n",
    "result (returned as a list in Python 2):\n",
    "\n",
    "[{'age': 7, 'name': 'Pam'}]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a6b435c-e0ae-4397-a9cb-00100731ee49",
   "metadata": {},
   "outputs": [],
   "source": [
    "### DICTIONARIES \n",
    "# Dictionary is an unordered collection of key-value pairs. \n",
    "# Each entry has a key and value. \n",
    "# A dictionary can be considered as a list with special index.\n",
    "# The keys must be unique and immutable. So we can use strings, numbers (int or float), or tuples as keys."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42093425-da94-44ef-a06e-fbbecec4a16a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Creating a dictionary\n",
    "# We can create a dictionary by providing 0 or more key value pairs between curly braces \n",
    "empty_dict = {}\n",
    "grades = {'John':'A', 'Emily':'A+', 'Betty':'B', 'Mike':'C', 'Ashley':'A'}\n",
    "grades\n",
    "# {'Ashley': 'A', 'Betty': 'B', 'Emily': 'A+', 'John': 'A', 'Mike': 'C'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbb17ecf-6163-4523-93d6-45906bcd6896",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Accessing the values\n",
    "# We access a value in a list by providing the index. \n",
    "# Similarly, in dictionaries, the values are accessed by using the keys.\n",
    "grades['John']\n",
    "# 'A'\n",
    "grades.get('Betty')\n",
    "# 'B'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b26bf848-52c7-4f7d-a7f7-563ef74e2d44",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. All values and/or all keys\n",
    "# The keys method is used to get all the keys.\n",
    "grades.keys()\n",
    "# dict_keys(['John', 'Emily', 'Betty', 'Mike', 'Ashley'])\n",
    "# The return object is a dict_keys object which is an iterable. \n",
    "# Thus, we can iterate over it in for loops.\n",
    "\n",
    "# Similarly, the values method returns all the values.\n",
    "grades.values()\n",
    "#dict_values(['A', 'A+', 'B', 'C', 'A'])\n",
    "\n",
    "# We cannot index on dict_keys or dict_values but we can convert them to a list and then use indexing.\n",
    "list(grades.values())[0]\n",
    "#'A'\n",
    "# The items method returns key-value pairs in tuples.\n",
    "grades.items()\n",
    "# dict_items([('John', 'A'), ('Emily', 'A+'), ('Betty', 'B'), ('Mike', 'C'), ('Ashley', 'A')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfa6721c-c32c-435b-bf83-713c5107c4e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Updating or adding an item\n",
    "# Dictionaries are mutable so we can update, add or delete items. \n",
    "# The syntax for updating or adding an item is the same. \n",
    "# If the given key exists in the dictionary, the value of the existing item is updated. \n",
    "# Otherwise, a new item (i.e. key-value pair) is created.\n",
    "\n",
    "grades['Edward'] = 'B+'\n",
    "grades['John'] = 'B'\n",
    "grades\n",
    "{'Ashley': 'A',\n",
    " 'Betty': 'B',\n",
    " 'Edward': 'B+',\n",
    " 'Emily': 'A+',\n",
    " 'John': 'B',\n",
    " 'Mike': 'C'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80bc7e54-b841-414f-b6a0-7db39e1e0e83",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Updating with a new dictionary\n",
    "# We can also pass a dictionary to the update function.\n",
    "# The dictionary will be updated based on the items in the new dictionary. It will become more clear with an examples.\n",
    "# Consider the following grades and grades_new dictionaries:\n",
    "grades = {'John':'A', 'Emily':'A+', 'Betty':'B', 'Mike':'C'}\n",
    "grades_new = {'John':'B', 'Sam':'A', 'Betty':'A'}\n",
    "# If we update grades based on grades_new, the values of John and Betty will be updated.\n",
    "# Also, a new item (‘Sam’:’A’) will be added.\n",
    "grades.update(grades_new)\n",
    "grades\n",
    "#{'Betty': 'A', 'Emily': 'A+', 'John': 'B', 'Mike': 'C', 'Sam': 'A'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6985f25f-7689-4a8e-be9b-38e44b682232",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 6. Deleting an item\n",
    "# We can use the del or pop function to delete an item. We just pass the key of the item to be deleted.\n",
    "del(grades['Edward'])\n",
    "grades.pop('Ashley')\n",
    "#'A'\n",
    "grades\n",
    "'Betty': 'B', 'Emily': 'A+', 'John': 'B', 'Mike': 'C'}\n",
    "# Unlike the del function, the pop function returns the value of the deleted item. \n",
    "# Thus, we have the option to assign it to a variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4d02bc1-4a60-4843-96e4-4c832d9d3a57",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 7. Dictionary as iterable\n",
    "# We can iterate over a dictionary. By default, the iteration is based on keys.\n",
    "for i in grades:\n",
    "    print(i)\n",
    "John\n",
    "Emily\n",
    "Betty\n",
    "Mike\n",
    "# We can also iterate over values (grades.values()) or key-value pairs (grades.items())."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7625e4c-0e0d-49a6-bc71-ca40863327da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8. Dictionary comprehension\n",
    "# It is similar to a list comprehension. \n",
    "# Dictionary comprehension is a way to create dictionaries based on iterables.\n",
    "{x: x**2 for x in range(5)}\n",
    "{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}\n",
    "{word: len(word) for word in ['data','science','is','awesome']}\n",
    "{'awesome': 7, 'data': 4, 'is': 2, 'science': 7}\n",
    "# The elements in the iterable become the keys of the dictionary. \n",
    "# The values are determined based on the assignment in the dictionary comprehension.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "499dac3c-0d83-4859-91fb-602678895cbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 9. Creating a dictionary from a list of lists\n",
    "# We can create a dictionary using a list of lists or list of tuples.\n",
    "a = [['A',4], ['B',5], ['C',11]]\n",
    "dict(a)\n",
    "{'A': 4, 'B': 5, 'C': 11}\n",
    "b = [('A',4), ('B',5), ('C',11)]\n",
    "dict(b)\n",
    "{'A': 4, 'B': 5, 'C': 11}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "900f33ef-e258-4fba-8b24-4a67960b3b00",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10. From dictionary to dataframe\n",
    "# The dataframe function of Pandas can be used to create a dataframe using a dictionary.\n",
    "# The keys become the column names and the values become rows.\n",
    "# Up until now, we have done examples with dictionaries whose values were strings.\n",
    "# However, the values in a dictionary can be of any type such as lists, numpy arrays, other dictionaries and so on.\n",
    "# In case of creating a dataframe from a dictionary, values consist of arrays (e.g. list, numpy array).\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "dict_a = {'names':['Amber','John','Edward','Emily'],\n",
    "         'points':np.random.randint(100, size=4)}\n",
    "df = pd.DataFrame(dict_a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43d78ebb-329c-4d55-8c53-420a3c3c3f5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 11. Len and clear\n",
    "# The len function returns the number of items in a dictionary (i.e. the length). \n",
    "# The clear method is used to delete all items from a dictionary so we will end up having an empty dictionary.\n",
    "len(grades)\n",
    "grades.clear()\n",
    "len(grades)\n",
    "# 0 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13e30aba-259a-45da-bcc4-ab1cee62059d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 12. Copying a dictionary\n",
    "grades = {'John':'A', 'Emily':'A+', 'Betty':'B'}\n",
    "dict1 = grades\n",
    "dict2 = grades.copy()\n",
    "dict3 = dict(grades)\n",
    "# All dict1, dict2, and dict3 contain the exactly same key-value pairs as grades.\n",
    "# However, dict1 is just a pointer to the key-value pairs in grades. Thus, any change in grades will also change dict1.\n",
    "# Dict2 and dict3 are separate objects in the memory so they will not be affected by the changes in grades."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2279b6ae-d437-411b-bda7-aa7433e83593",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 13 Looping into dicts \n",
    "# no method \n",
    "for x in mock_data:\n",
    "    print(x)\n",
    "# .keys() method - returns a dict_keys object that is then iterated over as we store each value in our x variable\n",
    "for x in mock_data.keys():\n",
    "    print(x)\n",
    "# using the .values() method will store the term’s value in x rather than the key.\n",
    "for x in mock_data.values():\n",
    "    print(x)\n",
    "# use the .items() method, which returns each key-value pair as a two-value tuple.\n",
    "for x in mock_data.items():\n",
    "    print(x)\n",
    "for k,v in mock_data.items():\n",
    "    print(k,v)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b8621d9-5886-4f75-b7cb-7205fbba4271",
   "metadata": {},
   "source": [
    "How to Boost Pandas Functions with Python Dictionaries \n",
    "https://towardsdatascience.com/how-to-boost-pandas-functions-with-python-dictionaries-35da25e250d7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d377a25-2bc8-4493-98fa-798f9f5f9a8e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c146a329-747f-41fa-8090-c2c28d6c1134",
   "metadata": {},
   "outputs": [],
   "source": [
    "# looping list \n",
    "# This method will not work for a dictionary because the data requires an iterable with positional values, but I wanted to include it for reference.\n",
    "mock_data = [90, 45, 32, 44]\n",
    "for i in range(len(data)):\n",
    "   print(data[i]) # 90, 45, 32, 44\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
