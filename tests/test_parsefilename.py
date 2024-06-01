"""
Test file for ParseFileName
"""

import unittest

import parsefilename.parsefilename as parsefilename
import re

class TestParseFileName(unittest.TestCase):

# Test Blender Scene regex
    correctBlendSceneName = "Max-01.blend"
    incorrectBlendSceneNames = [
        "Max-01.ma",
        "Max-1.blend",
        "Max-111.blend",
        "Max01.blend",
        "Max-01blend",
        "Max-01-blend",
        "-01.blend",
        "Max-.blend",
        "Max-01.",
        "Max-LaMenace-01.blend",
        ""
    ]

    def test_correct_reg_blend_scene(self):
        self.assertIsNotNone(re.search(parsefilename.REG_BLEND_SCENE, self.correctBlendSceneName))
        
    def test_incorrect_reg_blend_scene(self):
        for fileName in self.incorrectBlendSceneNames:         
            self.assertIsNone(re.search(parsefilename.REG_BLEND_SCENE, fileName))

# Test Blender FBX regex
    correctBlendFBXName = "Max-01.fbx"
    incorrectBlendFBXNames = [
        "Max-01.ma",
        "Max-1.fbx",
        "Max-111.fbx",
        "Max01.fbx",
        "Max-01fbx",
        "Max-01-fbx",
        "-01.fbx",
        "Max-.fbx",
        "Max-01.",
        "Max-LaMenace-01.fbx",
        ""
    ]

    def test_correct_reg_blend_fbx(self):
        self.assertIsNotNone(re.search(parsefilename.REG_BLEND_FBX, self.correctBlendFBXName))
        
    def test_incorrect_reg_blend_fbx(self):
        for fileName in self.incorrectBlendFBXNames:         
            self.assertIsNone(re.search(parsefilename.REG_BLEND_FBX, fileName))

# Test Anim Scene regex
    correctAnimSceneName = "Max-Running-001.ma"
    incorrectAnimSceneNames = [
        "Max-Running-001.blend",
        "Max-Running-01.ma",
        "Max-Running-1001.ma",
        "MaxRunning001.ma",
        "MaxRunning-001.ma",
        "Max-Running001.ma",
        "Max-Running-001ma",
        "Max-Running-001-ma",
        "-Running-001.ma",
        "Max--001.ma",
        "Max-001.ma",
        "Max--Running-001.ma",
        "Max_Running_001.ma",
        "",
    ]
    
    def test_correct_reg_anim_scene(self):
        self.assertIsNotNone(re.search(parsefilename.REG_ANIM_SCENE, self.correctAnimSceneName))
        
    def test_incorrect_reg_anim_scene(self):
        for fileName in self.incorrectAnimSceneNames:         
            self.assertIsNone(re.search(parsefilename.REG_ANIM_SCENE, fileName))

# Test Anim FBX regex
    correctAnimFBXName = "Max-Running-001.fbx"
    incorrectAnimFBXNames = [
        "Max-Running-001.blend",
        "Max-Running-01.fbx",
        "Max-Running-0101.fbx",
        "MaxRunning001.fbx",
        "MaxRunning-001.fbx",
        "Max-Running001.fbx",
        "Max-Running-001ma",
        "Max-Running-001-ma",
        "-Running-001.fbx",
        "Max--001.fbx",
        "Max-001.fbx",
        "Max--Running-001.fbx",
        "Max_Running_001.fbx",
        "",
    ]
    
    def test_correct_reg_anim_fbx(self):
        self.assertIsNotNone(re.search(parsefilename.REG_ANIM_FBX, self.correctAnimFBXName))
        
    def test_incorrect_reg_anim_fbx(self):
        for fileName in self.incorrectAnimFBXNames:         
            self.assertIsNone(re.search(parsefilename.REG_ANIM_FBX, fileName))

# Test Cinematic Asset regex
    correctCineAssetName = "DiscoveringTemple-Robin.uasset"
    incorrectCineAssetNames = [
        "DiscoveringTemple-Robin.fbx",
        "DiscoveringTemple-.uasset",
        "-Robin.uasset",
        "DiscoveringTemple.uasset",
        "DiscoveringTemple-Robin-01.uasset",
        "DiscoveringTemple-Robinuasset",
        "DiscoveringTemple-Robin-uasset",
        "DiscoveringTemple_Robin.uasset",
        ""
    ]
    
    def test_correct_reg_cine_asset(self):
        self.assertIsNotNone(re.search(parsefilename.REG_CINEMATIC_UASSET, self.correctCineAssetName))
        
    def test_incorrect_reg_cine_asset(self):
        for fileName in self.incorrectCineAssetNames:         
            self.assertIsNone(re.search(parsefilename.REG_CINEMATIC_UASSET, fileName))

#Test Parse Functions

# Test Parse Blend Scene

    def test_correct_parse_blend_scene(self):
        self.assertEqual(parsefilename._ParseFileNameBlenderScene("Max-01"), {"Character":{"name":"Max","version":"01"}})

    #def test_incorrect_parse_blend_scene(self):
    #    for fileName in self.incorrectBlendSceneNames:         
    #        self.assertRaises(parsefilename.ParseFileNameBlenderScene(fileName))


# Test Parse Blend FBX

    def test_correct_parse_blend_fbx(self):
        self.assertEqual(parsefilename._ParseFileNameBlenderFBX("Max-01"), {"Character":{"name":"Max","version":"01"}})

# Test Parse Anim Scene

    def test_correct_parse_anim_scene(self):
        self.assertEqual(parsefilename._ParseFileNameAnimScene("Max-Running-001"), {"Animation":{"action":"Running","version":"001"},"Character":{"name":"Max"}})

# Test Parse Anim FBX

    def test_correct_parse_anim_fbx(self):
        self.assertEqual(parsefilename._ParseFileNameAnimFBX("Max-Running-001"), {"Animation":{"action":"Running","version":"001"},"Character":{"name":"Max"}})

# Test Parse Cinematic Asset

    def test_correct_parse_cynematic_asset(self):
        self.assertEqual(parsefilename._ParseFileNameCinematic("DiscoveringTemple-Robin"), {"Cinematic":{"name":"DiscoveringTemple"}, "Character":{"name":"Robin"}})


# Test Final Function

    def test_correct_parse_all(self):
        self.assertEqual(parsefilename.ParseFileName("Max-01.blend"), {"Character":{"name":"Max","version":"01"}})
        self.assertEqual(parsefilename.ParseFileName("Max-01.fbx"), {"Character":{"name":"Max","version":"01"}})
        self.assertEqual(parsefilename.ParseFileName("Max-Running-001.ma"), {"Animation":{"action":"Running","version":"001"},"Character":{"name":"Max"}})
        self.assertEqual(parsefilename.ParseFileName("Max-Running-001.fbx"), {"Animation":{"action":"Running","version":"001"},"Character":{"name":"Max"}})
        self.assertEqual(parsefilename.ParseFileName("DiscoveringTemple-Robin.uasset"), {"Cinematic":{"name":"DiscoveringTemple"}, "Character":{"name":"Robin"}})

    def test_incorrect_parse_all(self):
        for fileName in self.incorrectBlendSceneNames:
            self.assertRaises(ValueError, parsefilename.ParseFileName, fileName)
            
        for fileName in self.incorrectBlendFBXNames:
            self.assertRaises(ValueError, parsefilename.ParseFileName, fileName)
            
        for fileName in self.incorrectAnimSceneNames:
            self.assertRaises(ValueError, parsefilename.ParseFileName, fileName)
            
        for fileName in self.incorrectAnimFBXNames:
            self.assertRaises(ValueError, parsefilename.ParseFileName, fileName)
            
        for fileName in self.incorrectCineAssetNames:
            self.assertRaises(ValueError, parsefilename.ParseFileName, fileName)


# Launch Test
if __name__ == "__main__":
    unittest.main()