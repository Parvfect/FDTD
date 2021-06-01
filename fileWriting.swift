import Foundation

var DataString: String = ""

public func AppendToString(dataString : String){
    DataString = DataString + dataString
}

public func writeToFile(FileURL : String, dataToWrite : String) -> Bool{
    
    let directoryURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
    let fileURL = URL(fileURLWithPath: FileURL, relativeTo: directoryURL)
    
    guard let data = dataToWrite.data(using: .utf8) else {
        return false
    }
    
    do {
        try data.write(to: fileURL)
        return true
    
    } catch {
        print(error.localizedDescription)
        return false
    }
}

