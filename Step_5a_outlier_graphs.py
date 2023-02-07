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
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# select numerical type variables
num_df = df.select_dtypes(include='int64')
num_list = list(num_df.columns)
print(num_list)

# plot histograms in one column, four attributes at a time (plus final residual)
row_count = len(num_list)
plot_count = int(row_count / 4)
residual = row_count % 4

# Select the z-score multiple that defines an outlier
alpha = 5

# Sequence of four attribute plots
for plot in range(plot_count):
    f, axes = plt.subplots(4, 1, figsize=(7, 7))
    for i in range(4):
        attr = num_list.pop()
        ax_row = i
        avg = num_df[attr].mean()
        vol = num_df[attr].std()
        lb = avg - alpha * vol
        rb = avg + alpha * vol
        sns.distplot(num_df[attr], ax=axes[ax_row])
        axes[ax_row].axvline(lb, color='r')
        axes[ax_row].axvline(rb, color='r')
    plt.savefig("outlier_plot_" + str(plot) + ".png")
# Final residual plot
f, axes = plt.subplots(residual, 1, figsize=(7, 7))
for i in range(residual):
    attr = num_list.pop()
    ax_row = i
    avg = num_df[attr].mean()
    vol = num_df[attr].std()
    lb = avg - alpha * vol
    rb = avg + alpha * vol
    sns.distplot(num_df[attr], ax=axes[ax_row])
    axes[ax_row].axvline(lb, color='r')
    axes[ax_row].axvline(rb, color='r')
plt.savefig("outlier_plot_" + str(plot + 1) + ".png")
