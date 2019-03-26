CREATE_EXECUTABLE_PROGRAM_ADT_XML='''<?xml version="1.0" encoding="UTF-8"?>
<program:abapProgram xmlns:program="http://www.sap.com/adt/programs/programs" xmlns:adtcore="http://www.sap.com/adt/core" adtcore:type="PROG/P" adtcore:description="Say hello!" adtcore:language="EN" adtcore:name="ZHELLO_WORLD" adtcore:masterLanguage="EN" adtcore:masterSystem="NPL" adtcore:responsible="FILAK" adtcore:version="active">
<adtcore:packageRef adtcore:name="$TEST"/>
<program:logicalDatabase>
<program:ref/>
</program:logicalDatabase>
</program:abapProgram>'''

GET_EXECUTABLE_PROGRAM_ADT_XML = '''<?xml version="1.0" encoding="utf-8"?>
<program:abapProgram xmlns:program="http://www.sap.com/adt/programs/programs" xmlns:abapsource="http://www.sap.com/adt/abapsource" xmlns:adtcore="http://www.sap.com/adt/core" program:lockedByEditor="false" program:programType="executableProgram" abapsource:sourceUri="source/main" abapsource:fixPointArithmetic="true" abapsource:activeUnicodeCheck="true" adtcore:responsible="FILAK" adtcore:masterLanguage="EN" adtcore:masterSystem="NPL" adtcore:name="ZHELLO_WORLD" adtcore:type="PROG/P" adtcore:changedAt="2019-02-10T20:16:33Z" adtcore:version="active" adtcore:createdAt="2019-01-30T00:00:00Z" adtcore:changedBy="DEVELOPER" adtcore:description="Say hello!" adtcore:descriptionTextLimit="70" adtcore:language="EN">
  <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="source/main/versions" rel="http://www.sap.com/adt/relations/versions"/>
  <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="source/main" rel="http://www.sap.com/adt/relations/source" type="text/plain" etag="201902102016330011"/>
  <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="source/main" rel="http://www.sap.com/adt/relations/source" type="text/html" etag="201902102016330011"/>
  <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="./zhello_world/objectstructure" rel="http://www.sap.com/adt/relations/objectstructure" type="application/vnd.sap.adt.objectstructure.v2+xml"/>
  <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="/sap/bc/adt/vit/wb/object_type/progpx/object_name/ZHELLO_WORLD" rel="http://www.sap.com/adt/relations/sources/textelements" type="application/vnd.sap.sapgui" title="Text Elements"/>
  <adtcore:packageRef adtcore:uri="/sap/bc/adt/packages/%24iamtheking" adtcore:type="DEVC/K" adtcore:name="$IAMTHEKING"/>
  <abapsource:syntaxConfiguration>
    <abapsource:language>
      <abapsource:version>X</abapsource:version>
      <abapsource:description>Standard ABAP voidsnicode)</abapsource:description>
      <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="/sap/bc/adt/abapsource/parsers/rnd/grammar" rel="http://www.sap.com/adt/relations/abapsource/parser" type="text/plain" title="Standard ABAP (Unicode)" etag="752"/>
    </abapsource:language>
  </abapsource:syntaxConfiguration>
  <program:logicalDatabase>
    <program:ref adtcore:name="D$S"/>
  </program:logicalDatabase>
</program:abapProgram>
'''
