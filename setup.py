from setuptools import setup, find_packages
import os

version = '1.0b13.dev0'

README = open("README.rst").read()
HISTORY = open(os.path.join("docs", "HISTORY.rst")).read()

setup(name='genweb.controlpanel',
      version=version,
      description="Package containing the Genweb UPC control panel.",
      long_description=README + "\n" + HISTORY,
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='theme genweb plone',
      author='UPCnet Plone Team',
      author_email='plone.team@upcnet.es',
      url='https://github.com/UPCnet/genweb.controlpanel.git',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['genweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'genweb.core',
          'plone.app.registry'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
