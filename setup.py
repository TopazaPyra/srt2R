#!/usr/bin/env python
# -*- coding:utf-8 -*-

from distutils.core import setup

setup(
      name='srt2R',
      version='0.4',
      description='Conversion de fichiers de tags srt vers R.',
      long_description='''Logiciel de conversion développé dans le cadre du laboratoire de recherche
      Topaza Pyra.
      
Les fichiers srt doivent au préalable avoir été créés à l\'aide d\'un éditeur
de sous-titres (par exemple subtitleeditor), en respectant la syntaxe indiquée
dans la documentation.

Srt2R génère un fichier csv pour chaque fichier srt, contenant les tags 
associés à leurs time-codes respectifs. Un fichier de syntaxe R est également
créé afin de faciliter l'import dans le logiciel de statistiques R.''',
      author='Johan Binard',
      author_email='j.binard@univ-lyon2.fr',
      url='https://github.com/TopazaPyra/srt2R',
      license='GNU General Public License (GPL)',
      packages=['srt2R'],
      scripts=['srt2r'],
      data_files=[ ('/usr/share/applications', ['srt2r.desktop']),('/usr/share/srt2R', ['srt2R.svg'])]
      )
