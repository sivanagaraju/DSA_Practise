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
    
    ' Assign the change event
    With cb.Object
        .OnChange = "ValidateComboBoxEntry"
    End With
End Sub

Sub ValidateComboBoxEntry()
    Dim cb As MSForms.ComboBox
    Set cb = Application.Caller
    
    Dim enteredValue As String
    enteredValue = cb.Text
    
    ' If nothing entered, exit
    If enteredValue = "" Then Exit Sub
    
    ' Check if value exists in list
    Dim valueExists As Boolean
    Dim i As Long
    valueExists = False
    
    For i = 0 To cb.ListCount - 1
        If StrComp(cb.List(i), enteredValue, vbTextCompare) = 0 Then
            valueExists = True
            ' Set the exact case from the list
            cb.Text = cb.List(i)
            Exit For
        End If
    Next i
    
    ' If value doesn't exist, clear the combobox
    If Not valueExists Then
        cb.Text = ""
    End If
    
    ' Update the cell value
    Dim cellAddress As String
    cellAddress = Replace(cb.Name, "DataCombo", "")
    Range(cellAddress).Value = cb.Text
End Sub

Private Sub Worksheet_Change(ByVal Target As Range)
    ' This event will handle any direct changes to the cells
    Dim obj As OLEObject
    Dim cellAddress As String
    
    On Error Resume Next
    For Each obj In ActiveSheet.OLEObjects
        If TypeName(obj.Object) = "ComboBox" Then
            cellAddress = Replace(obj.Name, "DataCombo", "")
            If Not Range(cellAddress).Value = obj.Object.Value Then
                obj.Object.Value = Range(cellAddress).Value
            End If
        End If
    Next obj
    On Error GoTo 0
End Sub