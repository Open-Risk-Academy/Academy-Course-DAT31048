# (c) 2019 - 2022 Open Risk (https://www.openriskmanagement.com)
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
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# select the numerical variables
num_df = df.select_dtypes(include='int64')
num_list = list(num_df.columns)
print(num_list)

# plot histograms in three columns
row_count = 1 + int(len(num_list) / 3)
f, axes = plt.subplots(row_count, 3, figsize=(7, 7))
for attr in num_list:
    i = num_list.index(attr)
    ax_col = i % 3
    # if ax_col == 0:
    #     ax_col = 3
    ax_row = int((i - ax_col) / 3)
    print(i, attr, (ax_row, ax_col))
    sns.distplot(num_df[attr], ax=axes[ax_row, ax_col])
plt.savefig("numerical_variable_histograms.png")

# select the categorical variables
cat_df = df.select_dtypes(include='category')
cat_list = list(cat_df.columns)
print(cat_list)

# plot histograms in three columns
row_count = 1 + int(len(cat_list) / 3)
f, axes = plt.subplots(row_count, 3, figsize=(7, 7))
for attr in cat_list:
    i = cat_list.index(attr)
    ax_col = i % 3
    # if ax_col == 0:
    #     ax_col = 3
    ax_row = int((i - ax_col) / 3)
    print(i, attr, (ax_row, ax_col))
    dd = cat_df[attr].value_counts()
    x = dd.index
    y = dd.values
    sns.barplot(x=x, y=y, ax=axes[ax_row, ax_col])
plt.savefig("categorical_variable_barplots.png")
