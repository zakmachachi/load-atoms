C-GAP-17
========

Complete dataset for training and testing the C-GAP-17 model. 
For details, see the supplementary information here:
https://doi.org/10.17863/CAM.7453


.. code-block:: python

    >>> from load_atoms import dataset
    >>> dataset("C-GAP-17")
    C-GAP-17:
        structures: 4,530
        atoms: 284,965
        species:
            C: 100.00%
        properties:
            per atom: (force)
            per structure: (detailed_ct, energy, split, config_type)



This dataset is licensed under the CC BY-NC-SA 4.0 license.



.. code-block:: bibtex

    @article{Deringer-17,
        title = {Machine learning based interatomic potential for amorphous carbon},
        doi = {10.1103/PhysRevB.95.094203},
        volume = {95},
        number = {9},
        urldate = {2021-07-15},
        journal = {Physical Review B},
        author = {Deringer, Volker L. and Cs{\'a}nyi, G{\'a}bor},    
        year = {2017},
        pages = {094203},
    }
