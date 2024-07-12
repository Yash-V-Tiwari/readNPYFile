function data = readNPYFile(filename)

npyFilePath = append("'", filename, "'");
pyrunfile(append("npyReader.py ", npyFilePath));

csvFilePath = append(filename(1:end-3), "csv");
T = readtable(csvFilePath, 'Decimal','.', 'Delimiter',',');
S = table2struct(T);
data = S;

delete(csvFilePath);