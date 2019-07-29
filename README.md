# Klima_Perny_Voggenberger
## Implementierung der Analog Methode anhand der ERA5 Reanalyse Daten und Validierung mit dem Spartacus Datensatz
**get_data.ipynb**: Herunterladen des ERA5 Reanalyse Datensatzes über das *Climate Data Store Application Program Interface* (CDS API) <br>
<br>
**Create_small_data.ipynb**: Für Testzwecke den großen ERA5 Datensatz in einen kleine 3x3 Gitter Datensatz schneiden und aus stündlichen Werte Tagesmittel bilden <br>
<br>
**Preprocessing.ipynb**: Bildung der Anomalien aus dem kleinen Datensatz<br>
<br>
**preprocessing_validation.ipynb**: Darstellen der Anomalien mittels geoview <br>
<br>
**Analog Methode**: Implementierung der Analog Methode sowie Beschreibung dieser <br>
<br>
**Validation with Spartacus**: Validierung mit dem Spartacus Datensatz für ein Jahr <br>
<br>
**Daten**:  <br>
*Analoga.p* - gefundene Analog-Tage (3 Analoga)<br>
*me_verif.p* - Mittlerer Fehler für das Jahr 2015<br>
*mae_verif.p* - Mittlerer absoluter Fehler für das Jahr 2015<br>
*rmse_verif.p* - Root Mean Square Error für das Jahr 2015<br>
*corr_verif.p* - Correlationskoeffizienten für das Jahr 2015<br>
