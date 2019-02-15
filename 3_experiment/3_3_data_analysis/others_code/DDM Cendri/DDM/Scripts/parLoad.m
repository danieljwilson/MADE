function Data = parLoad(fileName, varargin)
    Data = load(fileName);
    
    if ~isempty(varargin)
        vars = fieldnames(Data);
        rmvars = setdiff(varargin{1}, vars);
        Data = rmfield(Data, rmvars);
    end
end