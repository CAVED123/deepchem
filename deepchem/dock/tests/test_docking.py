"""
Tests for Docking 
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

__author__ = "Bharath Ramsundar"
__copyright__ = "Copyright 2016, Stanford University"
__license__ = "GPL"

import unittest
import tempfile
import os
import shutil
import numpy as np
import sys
import deepchem as dc

class TestDocking(unittest.TestCase):
  """
  Does sanity checks on pose generation. 
  """
  def test_vina_grid_rf_docker_init(self):
    """Test that VinaGridRFDocker can be initialized."""
    if sys.version_info >= (3,0):
      return
    docker = dc.dock.VinaGridRFDocker()

  def test_vina_grid_dnn_docker_init(self):
    """Test that VinaGridDNNDocker can be initialized."""
    docker = dc.dock.VinaGridDNNDocker()

  def test_vina_grid_rf_docker_dock(self):
    """Test that VinaGridRFDocker can dock."""
    if sys.version_info >= (3,0):
      return
    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    protein_file = os.path.join(current_dir, "1jld_protein.pdb")
    ligand_file = os.path.join(current_dir, "1jld_ligand.sdf")

    docker = dc.dock.VinaGridRFDocker()
    (score, (protein_docked, ligand_docked)) = docker.dock(
        protein_file, ligand_file)

    # Check returned files exist
    print("(score, (protein_docked, ligand_docked))")
    print((score, (protein_docked, ligand_docked)))
    assert score.shape == (1,)
    assert os.path.exists(protein_docked)
    assert os.path.exists(ligand_docked)

  def test_vina_grid_dnn_docker_dock(self):
    """Test that VinaGridDNNDocker can dock."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    protein_file = os.path.join(current_dir, "1jld_protein.pdb")
    ligand_file = os.path.join(current_dir, "1jld_ligand.sdf")

    docker = dc.dock.VinaGridDNNDocker()
    (score, (protein_docked, ligand_docked)) = docker.dock(
        protein_file, ligand_file)

    # Check returned files exist
    print("(score, (protein_docked, ligand_docked))")
    print((score, (protein_docked, ligand_docked)))
    assert score.shape == (1,)
    assert os.path.exists(protein_docked)
    assert os.path.exists(ligand_docked)