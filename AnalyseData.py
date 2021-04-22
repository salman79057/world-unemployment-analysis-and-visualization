import pandas as pd

class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        if(path == 'datasets/unemployment2020.csv'):
            self.cleanData2020()

    def cleanData2020(self):
        self.df.columns = [col.title() for col in self.df.columns.values]
        self.df.rename(columns={'Subject' : 'Gender', 'Value' : 'Unemployment Rate'}, inplace=True)
        self.df.drop(columns=['Indicator', 'Measure', 'Flag Codes', 'Frequency'], inplace=True)
        self.df['Month'] = ""
        Months = ['January','February','March','April','May','June','July','August','September','October']

        month = []

        for row in self.df.Time:
            if row == '2020-01':
                month.append(Months[0])
            elif row == '2020-02':
                month.append(Months[1])
            elif row == '2020-03':
                month.append(Months[2])
            elif row == '2020-04':
                month.append(Months[3])
            elif row == '2020-05':
                month.append(Months[4])
            elif row == '2020-06':
                month.append(Months[5])
            elif row == '2020-07':
                month.append(Months[6])
            elif row == '2020-08':
                month.append(Months[7])
            elif row == '2020-09':
                month.append(Months[8])
            elif row == '2020-10':
                month.append(Months[9])
            else:
                month.append('Not Defined')

        self.df.Month = month

        self.df.tail(5)

    def getCategories(self):
        return self.df.groupby('Category').count().sort_values('App')['App'][::-1]

    def getCountrywise(self, month):
        return self.df[self.df['Month'] == month].groupby('Location').sum().sort_values('Unemployment Rate', ascending = False)

    def getDataset(self):
        return self.df