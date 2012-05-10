from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='genweb.controlpanel',
      version=version,
      description="Package containing the Genweb UPC control panel.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
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
          'plone.app.registry'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
