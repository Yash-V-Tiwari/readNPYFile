function data = readMetadataNPY(filename)

pyrunfile(append("npyReader.py ", filename));

[file,path] = uigetfile();
if isequal(file,0)
   disp('User selected Cancel');
else
   %csvFilePath = append(filename(1:end-3), "csv");
   T = readtable(fullfile(path,file), 'Decimal','.', 'Delimiter',',');
   S = struct('Crossing_Point',T.Crossing_Point, 'Crossing_level',T.Crossing_level, ...
           'Threshold',T.Threshold, 'Direction',T.Direction, 'Learning_rate',T.Learning_rate);
   data = S;
end
