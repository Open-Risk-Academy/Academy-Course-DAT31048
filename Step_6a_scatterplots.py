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
import pandas as pd
import seaborn as sns

# Load the data from hdf file
df = pd.read_hdf('german_credit.h5', 'df')

# A standard scatterplot of numerical variables
sns.scatterplot(x=df['A5'], y=df['A13'])
plt.savefig("standard_scatter_plot.png")

# Illustration of the problem with scatterplots of categorical variables
sns.scatterplot(x=df['A3'], y=df['A12'])
plt.savefig("failed_scatter_plot.png")
