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

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# Get the statistics of numerical variables
print(df.describe(include='int64'))
# Save to file for closer inspection
df.describe(include='int64').to_csv("univariate_stats1.csv")

# Get the statistics of categorical variables
print(df.describe(include='category'))
df.describe(include='category').to_csv("univariate_stats2.csv")
