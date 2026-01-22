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

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# Convert these columns to 'category' dtype because the columns were not explicitly converted to 'category' data type after loading the DataFrame from the HDF5 file in this cell
df[categorical_cols_new_names] = df[categorical_cols_new_names].astype('category')

# select the numerical variables
num_df = df.select_dtypes(include='int64')
num_list = list(num_df.columns)
print(num_list)

# plot histograms in three columns
row_count = 1 + int(len(num_list) / 3)
f, axes = plt.subplots(row_count, 3, figsize=(15, 5 * row_count))
axes = axes.flatten() # Flatten the axes array for easier iteration
# use sns.histplot instead of sns.displot as sns.displot function is meant for creating standalone figures, not for plotting on specific axes within a matplotlib subplot grid
for i, attr in enumerate(num_list):
    sns.histplot(num_df[attr], ax=axes[i])
    axes[i].set_title(f'Histogram of {attr}')
plt.tight_layout()
plt.savefig("numerical_variable_histograms.png")

# select the categorical variables
cat_df = df.select_dtypes(include='category')
cat_list = list(cat_df.columns)
print(cat_list)

# plot barplots in three columns
row_count = 1 + int(len(cat_list) / 3)
f, axes = plt.subplots(row_count, 3, figsize=(15, 5 * row_count))
axes = axes.flatten() # Flatten the axes array for easier iteration

for i, attr in enumerate(cat_list):
    dd = cat_df[attr].value_counts()
    x = dd.index
    y = dd.values
    sns.barplot(x=x, y=y, ax=axes[i])
    axes[i].set_title(f'Barplot of {attr}')
    axes[i].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig("categorical_variable_barplots.png")
