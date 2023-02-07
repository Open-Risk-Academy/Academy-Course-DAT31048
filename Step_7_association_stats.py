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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.stats.contingency_tables as sct
from statsmodels.graphics.mosaicplot import mosaic

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')
# We will assume all variables are categorical
df = df.astype('category')

# The default statistics
print('=' * 80)
print(df['A21'].describe())

# select an attribute and create a crosstab (contingency table) for reporting
print('=' * 80)
attr = 'A4'
ct = pd.crosstab(columns=df['A21'], index=df[attr], margins=True, margins_name="Total")
attr_list = list(ct.index)
attr_list.remove('Total')
print('Attribute ', attr, 'Value List: ', attr_list)
print('=' * 80)

#
# compute the chi-square test
#

ct0 = pd.crosstab(columns=df['A21'], index=df[attr])
chi2_test = st.chi2_contingency(ct0)
print('Expected Frequencies', chi2_test[3])
print('-' * 80)

#
# compute the chi-square contributions
#
table = sct.Table(ct0)
print('chi-square contributions: ', table.chi2_contribs)

#
# Create a new frame with the expected values if the attribute and default
# where independent
#
df0 = pd.DataFrame(chi2_test[3], columns=ct0.columns, index=ct0.index)

#
# Append the expected values of Good and Bad outcomes
#

ct[['Expected_Bads', 'Expected_Goods']] = df0
columns = ['Bads', 'Goods', 'Total', 'Expected_Bads', 'Expected_Goods']
ct.columns = columns

#
# Add further required derived measures to the frame
#
ct.loc[('Total', 'Expected_Bads')] = ct['Expected_Bads'].sum()
ct.loc[('Total', 'Expected_Goods')] = ct['Expected_Goods'].sum()
ct['Attr_Share'] = ct['Total'] / ct.loc[('Total', 'Total')]
ct['Bad_Rate'] = ct['Bads'] / ct['Total']
ct['Good_Rate'] = ct['Goods'] / ct['Total']
ct['Distr_Bad'] = ct['Bads'] / ct.loc[('Total', 'Bads')]
ct['Distr_Good'] = ct['Goods'] / ct.loc[('Total', 'Goods')]
ct['WoE'] = np.log(ct['Distr_Good'] / ct['Distr_Bad'])
print('=' * 80)
print(ct)
print('=' * 80)
Information_Value = (ct['WoE'] * (ct['Distr_Good'] - ct['Distr_Bad'])).sum()
print('chi-square ', chi2_test[0])
print('p-value ', chi2_test[1])
print('Degrees of Freedom ', chi2_test[2])
print('Information Value: ', Information_Value)

# Visualization
data = pd.crosstab(columns=df['A21'], index=df['A4'])
mosaic(data.stack(), title='A4 vs A21')
plt.savefig("mosaic_association_plot.png")
