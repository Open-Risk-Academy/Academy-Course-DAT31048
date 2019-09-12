# (c) 2019 Open Risk (https://www.openriskmanagement.com)
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

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# select numerical type variables
num_df = df.select_dtypes(include='int64')
num_list = list(num_df.columns)
print(num_list)

# Select the z-score multiple that defines an outlier
alpha = 5

print(80*'=')
print("Data Outliers")
print(80*'=')
for attr in num_list:
    avg = num_df[attr].mean()
    vol = num_df[attr].std()
    lb = avg - alpha * vol
    rb = avg + alpha * vol
    # Right boundary outliers
    right_outlier_no = len(num_df[attr].pipe(lambda x: x[x > rb]))
    # Left boundary outliers
    left_outlier_no = len(num_df[attr].pipe(lambda x: x[x < lb]))
    print(attr, left_outlier_no, right_outlier_no)
    if right_outlier_no > 0:
        print('Right Boundary Outliers ', num_df[attr].pipe(lambda x: x[x > rb]).values)
    print(80 * '.')
    if left_outlier_no > 0:
        print('Left Boundary Outliers ', num_df[attr].pipe(lambda x: x[x < lb]).values)
    print(80 * '.')



