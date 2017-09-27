from scene import *
import ui

class FirstScene(Scene):
    def setup(self):
		self.background = SpriteNode(position =self.size / 2,
		                                       color = (0.61, 0.78, 0.87),
		                                       parent = self,
		                                       size = self.size)
		
		self.school_crest = SpriteNode('./assets/sprites/school_crest.jpg',
		                               parent = self,
		                               position = self.size / 2)
		
    def touch_moved(self, touch):
# happens when your finger is moving around screen
# ..use when deploying app for Xcode and the App Store 
      self.school_crest.position = touch.location

main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH') 
main_view.add_subview(scene_view)
scene_view.scene = FirstScene() 
main_view.present(hide_title_bar = True, animated = False)
