# importar librerias
import pandas as pd
import numpy as np
from datetime import datetime
import datetime
from scipy import stats
import holidays
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from sklearn.impute import KNNImputer

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')
from ydata_profiling import ProfileReport