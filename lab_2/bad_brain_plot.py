import nilearn
from nilearn import plotting
import nibabel

# Load the image
img = nibabel.load('~\Desktop\BIOS278\BIOS_278_Lab_Amanda\lab_2\scan1.nii.gz')

# Plot it
plotting.plot_anat(img)
plotting.show()

# Save figure
display = plotting.plot_stat_map(img, threshold=3)
display.savefig('output.png')