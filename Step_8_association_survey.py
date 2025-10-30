# (c) 2019 - 2025 Open Risk (https://www.openriskmanagement.com)
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

import numpy as np
import pandas as pd
import scipy.stats as st

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')
# We will assume all variables are categorical
df = df.astype('category')

attributes = list(df.columns)
attributes.pop(attributes.index('A21'))

attribute_name = []
attribute_values = []
attribute_chi_squared = []
attribute_p_value = []
attribute_info_value = []

for attr in attributes:
    ct = pd.crosstab(columns=df['A21'], index=df[attr], margins=True, margins_name="Total")
    attr_list = list(ct.index)
    attr_list.remove('Total')
    cat_no = len(attr_list)
    if cat_no <= 15:
        ct0 = pd.crosstab(columns=df['A21'], index=df[attr])
        chi2_test = st.chi2_contingency(ct0)
        df1 = pd.DataFrame(chi2_test[3], columns=ct0.columns, index=ct0.index)
        ct[['Expected_Bads', 'Expected_Goods']] = df1
        columns = ['Bads', 'Goods', 'Total', 'Expected_Bads', 'Expected_Goods']
        ct.columns = columns
        ct.loc[('Total', 'Expected_Bads')] = ct['Expected_Bads'].sum()
        ct.loc[('Total', 'Expected_Goods')] = ct['Expected_Goods'].sum()
        ct['Attr_Share'] = ct['Total'] / ct.loc[('Total', 'Total')]
        ct['Bad_Rate'] = ct['Bads'] / ct['Total']
        ct['Good_Rate'] = ct['Goods'] / ct['Total']
        ct['Distr_Bad'] = ct['Bads'] / ct.loc[('Total', 'Bads')]
        ct['Distr_Good'] = ct['Goods'] / ct.loc[('Total', 'Goods')]
        ct['WoE'] = np.log(ct['Distr_Good'] / ct['Distr_Bad'])
        Information_Value = (ct['WoE'] * (ct['Distr_Good'] - ct['Distr_Bad'])).sum()
        attribute_name.append(attr)
        attribute_values.append(cat_no)
        attribute_chi_squared.append(chi2_test[0])
        attribute_p_value.append(chi2_test[1])
        attribute_info_value.append(Information_Value)

d = {'Attribute': attribute_name, 'Values': attribute_values, 'Chi-Squared': attribute_chi_squared,
     'P-Value': attribute_p_value, 'Info-Value': attribute_info_value}
df = pd.DataFrame(data=d)
