Option Explicit

' Add reference to Microsoft ActiveX Data Objects (ADODB) in VBA Editor (Tools > References)
Private Sub Worksheet_Activate()
    Call PopulateComboBox
End Sub

Sub PopulateComboBox()
    ' Create the ComboBox if it doesn't exist
    Dim cb As OLEObject
    On Error Resume Next
    Set cb = ActiveSheet.OLEObjects("DataComboBox")
    On Error GoTo 0
    
    If cb Is Nothing Then
        Set cb = ActiveSheet.OLEObjects.Add( _
            ClassType:="Forms.ComboBox.1", _
            Link:=False, _
            DisplayAsIcon:=False, _
            Left:=Range("A1").Left, _
            Top:=Range("A1").Top, _
            Width:=Range("A1").Width, _
            Height:=Range("A1").Height)
        cb.Name = "DataComboBox"
    End If
    
    ' Database Connection
    Dim conn As ADODB.Connection
    Dim rs As ADODB.Recordset
    Dim connectionString As String
    
    ' Replace these with your SQL Server details
    connectionString = "Provider=SQLOLEDB;" & _
                      "Server=YourServerName;" & _
                      "Database=YourDatabaseName;" & _
                      "Trusted_Connection=Yes;"  ' For Windows Authentication
    ' If using SQL Authentication, use this connection string instead:
    ' connectionString = "Provider=SQLOLEDB;" & _
    '                   "Server=YourServerName;" & _
    '                   "Database=YourDatabaseName;" & _
    '                   "User ID=YourUsername;" & _
    '                   "Password=YourPassword;"
    
    ' Create and open the connection
    Set conn = New ADODB.Connection
    conn.Open connectionString
    
    ' Create and execute the recordset
    Set rs = New ADODB.Recordset
    
    ' Replace with your actual SQL query
    Dim sqlQuery As String
    sqlQuery = "SELECT ColumnName FROM YourTable"
    
    rs.Open sqlQuery, conn
    
    ' Clear existing items
    cb.Object.Clear
    
    ' Populate combobox with data from recordset
    Do While Not rs.EOF
        cb.Object.AddItem rs.Fields(0).Value
        rs.MoveNext
    Loop
    
    ' Clean up
    rs.Close
    conn.Close
    Set rs = Nothing
    Set conn = Nothing
End Sub

Sub ComboBox_Change()
    ' Handle combobox selection change
    Dim selectedValue As String
    selectedValue = ActiveSheet.OLEObjects("DataComboBox").Object.Value
    
    ' Do something with the selected value
    ' For example, write it to a cell
    Range("B1").Value = selectedValue
End Sub