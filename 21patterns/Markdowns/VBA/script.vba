Option Explicit

' Add reference to Microsoft ActiveX Data Objects 6.1 in VBA Editor (Tools > References)
Private Sub Worksheet_Activate()
    Call CreateColumnComboBoxes
End Sub

Sub CreateColumnComboBoxes()
    Const TARGET_COLUMN As String = "A"  ' Change this to your desired column
    Const FIRST_ROW As Long = 2         ' Start from row 2 (assuming row 1 is header)
    
    Dim lastRow As Long
    lastRow = Cells(Rows.Count, TARGET_COLUMN).End(xlUp).Row
    
    RemoveExistingComboBoxes
    
    Dim comboList As Collection
    Set comboList = GetSQLData()
    
    Dim i As Long
    For i = FIRST_ROW To lastRow
        CreateSingleComboBox TARGET_COLUMN & i, comboList
    Next i
End Sub

Sub RemoveExistingComboBoxes()
    Dim obj As OLEObject
    
    On Error Resume Next
    For Each obj In ActiveSheet.OLEObjects
        If Left(obj.Name, 8) = "DataCombo" Then
            obj.Delete
        End If
    Next obj
    On Error GoTo 0
End Sub

Function GetSQLData() As Collection
    Dim conn As ADODB.Connection
    Dim rs As ADODB.Recordset
    Dim connectionString As String
    Dim result As New Collection
    
    connectionString = "Provider=SQLOLEDB;" & _
                      "Server=YourServerName;" & _
                      "Database=YourDatabaseName;" & _
                      "Trusted_Connection=Yes;"
    
    Set conn = New ADODB.Connection
    conn.Open connectionString
    
    Set rs = New ADODB.Recordset
    
    ' Replace with your actual SQL query
    Dim sqlQuery As String
    sqlQuery = "SELECT ColumnName FROM YourTable"
    
    rs.Open sqlQuery, conn
    
    Do While Not rs.EOF
        result.Add rs.Fields(0).Value
        rs.MoveNext
    Loop
    
    rs.Close
    conn.Close
    Set rs = Nothing
    Set conn = Nothing
    
    Set GetSQLData = result
End Function

Sub AddNewValueToDatabase(newValue As String)
    Dim conn As ADODB.Connection
    Dim cmd As ADODB.Command
    Dim connectionString As String
    
    connectionString = "Provider=SQLOLEDB;" & _
                      "Server=YourServerName;" & _
                      "Database=YourDatabaseName;" & _
                      "Trusted_Connection=Yes;"
    
    Set conn = New ADODB.Connection
    conn.Open connectionString
    
    Set cmd = New ADODB.Command
    With cmd
        .ActiveConnection = conn
        .CommandType = adCmdText
        ' Modify this INSERT statement according to your table structure
        .CommandText = "INSERT INTO YourTable (ColumnName) VALUES (?)"
        .Parameters.Append .CreateParameter("@Value", adVarChar, adParamInput, 255, newValue)
        .Execute
    End With
    
    conn.Close
    Set cmd = Nothing
    Set conn = Nothing
End Sub

Sub CreateSingleComboBox(cellAddress As String, comboList As Collection)
    Dim cb As OLEObject
    Dim targetCell As Range
    Set targetCell = Range(cellAddress)
    
    Set cb = ActiveSheet.OLEObjects.Add( _
        ClassType:="Forms.ComboBox.1", _
        Link:=False, _
        DisplayAsIcon:=False, _
        Left:=targetCell.Left, _
        Top:=targetCell.Top, _
        Width:=targetCell.Width, _
        Height:=targetCell.Height)
    
    cb.Name = "DataCombo" & Replace(cellAddress, "$", "")
    
    ' Enable text input
    cb.Object.Style = fmStyleDropDownCombo
    
    Dim item As Variant
    For Each item In comboList
        cb.Object.AddItem item
    Next item
    
    If Not IsEmpty(targetCell.Value) Then
        cb.Object.Value = targetCell.Value
    End If
End Sub

Private Sub Worksheet_Change(ByVal Target As Range)
    Dim obj As OLEObject
    Dim cellAddress As String
    Dim newValue As String
    Dim existingValues As Collection
    
    On Error Resume Next
    For Each obj In ActiveSheet.OLEObjects
        If TypeName(obj.Object) = "ComboBox" Then
            cellAddress = Replace(obj.Name, "DataCombo", "")
            
            ' Get the new value from the combobox
            newValue = obj.Object.Value
            
            ' If there's a new value
            If newValue <> "" Then
                ' Check if this value already exists in the combobox list
                Dim valueExists As Boolean
                valueExists = False
                
                Dim i As Long
                For i = 0 To obj.Object.ListCount - 1
                    If obj.Object.List(i) = newValue Then
                        valueExists = True
                        Exit For
                    End If
                Next i
                
                ' If it's a new value
                If Not valueExists Then
                    ' Ask user for confirmation
                    Dim response As VbMsgBoxResult
                    response = MsgBox("Add '" & newValue & "' to the list?", _
                                    vbQuestion + vbYesNo, "Add New Value")
                    
                    If response = vbYes Then
                        ' Add to database
                        AddNewValueToDatabase newValue
                        
                        ' Add to combobox
                        obj.Object.AddItem newValue
                        obj.Object.Value = newValue
                        
                        ' Update cell
                        Range(cellAddress).Value = newValue
                    End If
                Else
                    ' Update cell with existing value
                    Range(cellAddress).Value = newValue
                End If
            End If
        End If
    Next obj
    On Error GoTo 0
End Sub