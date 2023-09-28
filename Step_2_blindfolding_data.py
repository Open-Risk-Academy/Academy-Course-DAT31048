# (c) 2019 - 2023 Open Risk (https://www.openriskmanagement.com)
#
# This code is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of the course. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd

# Load the file into a pandas dataframe
df = pd.read_csv('german_credit.csv')

# Let us get a list of all variables names
headers = list(df)

# This is what we should get
"""
    A21: Creditability
    A1: Account Balance
    A2: Duration of Credit (month)
    A3: Payment Status of Previous Credit
    A4: Purpose
    A5: Credit Amount
    A6: Value Savings/Stocks
    A7: Length of current employment
    A8: Instalment per cent
    A9: Sex & Marital Status
    A10: Guarantors
    A11: Duration in Current address
    A12: Most valuable available asset
    A13: Age (years)
    A14: Concurrent Credits
    A15: Type of apartment
    A16: No of Credits at this Bank
    A17: Occupation
    A18: No of dependents
    A19: Telephone
    A20: Foreign Worker
"""

# Adding indicator of whether a variable is categorical or numerical in nature
# This is information we must get from the data documentation as it is not stored in CSV
variable_type = [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1]
categorical_list = []
for i in range(len(variable_type)):
    # print(i, headers[i])
    if variable_type[i] == 1:
        categorical_list.append(headers[i])
df[categorical_list] = df[categorical_list].astype('category')

# Rename the columns
# The first variable is the target variable which we give the label A21
variable_name = ['A21']
# The next variables are simply labeled sequentially from A1 to A20
for i in range(1, 21):
    variable_name.append('A' + str(i))
df.columns = variable_name

# Check
print(df.head(1))

# Save as hdf file
cstore = pd.HDFStore('german_credit.h5', mode='w')
cstore.append('df', df, format='table')
cstore.close()
