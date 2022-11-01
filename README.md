# vae

This project ingests a select few lunar surface temperature profiles, collected during the <a href = "https://www.jpl.nasa.gov/missions/diviner-lunar-radiometer-experiment-dlre">Diviner Lunar Radiometer Experiment</a>. The goal of this project is to train a Variational Autoencoder (VAE) on these profiles and to then explore the latent space created by the resultant model to understand if some physically informed trends can and have been learned by the unsupervised model. A potential extention of this project involves introducing physically informed loss functions to further constrain and expedite this learning. This is currently a work in progress, incumbent upon the results of some physics-based/mechanistic models which will serve as the ground truth.

Lunar surface temperature profiles are of a select few craters that were deemed areas of interest by Ben Moseley. Details on area selection are outlined in Append B of the following publication entitled <a href = "https://iopscience.iop.org/article/10.3847/PSJ/ab9a52"><i>Unsupervised Learning for Thermophysical Analysis on the Lunar Surface</i></a>. In this repository, we recreate the methodology outlined in this publication and set the stage for deploying the use of a trained VAE for the interpoation of lunar surface temperatures, specifically when observations at local noon (i.e. time of peak temperature) are missing. The accompanying slide deck can be used as a synopsis of this process.
