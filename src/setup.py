from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.Blindscan'
setup(name='enigma2-plugin-systemplugins-blindscan',
       version='3.0',
       description='blindscan...',
       package_dir={pkg: 'Blindscan'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'LICENSE.GPLv2']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
