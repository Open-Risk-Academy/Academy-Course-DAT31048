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
import seaborn as sns

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# Drop the target variable
ndf = df.drop(['A21'], axis=1)

# Get the correlation estimates using different methods. Options are
# Pearson Rho
# Kendall Tau
# Spearman Rank
# Plot a heatmap of the correlation matrix

corr = ndf.corr(method='spearman')
sns.heatmap(corr, cmap='Blues')
# plt.savefig("correlation_heatmap.png")

# number of computed correlations
n = len(corr.columns)

# identify outlier correlation pairs
for i in range(n):
    for j in range(i, n):
        if i != j and corr.iloc[i, j] > 0.5 or corr.iloc[i, j] < -0.3:
            print(corr.index[i], corr.columns[j], corr.iloc[i, j])
