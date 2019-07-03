function parSave(fileName, saveVar)
    SimData = saveVar;
    save(fileName, 'SimData');
end