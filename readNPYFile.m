function data = readNPYFile(filename)

% Encapsulates filename with "'" to support paths with whitespace. 
npyFilePath = append("'", filename, "'");  
% Call python script with correct file path.
pyrunfile(append("npyReader.py ", npyFilePath)); 

% Reads temp .csv file and constructs a struct.
csvFilePath = append(filename(1:end-3), "csv");
T = readtable(csvFilePath, 'Decimal','.', 'Delimiter',',');
S = table2struct(T);
data = S;

% deletes temp .csv file.
delete(csvFilePath);