+++
# Date this page was created.
date = "2018-01-01"

# Project title.
title = "Innovative Advanced Control of Large Cryogenic Systems"

# Project summary to display on homepage.
summary = "The ANR CRYOGREEN project gathers collaborative academic and industrial partners, including GIPSA-lab, CEA and CERN. We target to advanced control of large cryogenic systems via explicit nonlinear and hierarchical distributed model predictive control frameworks."

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = ""

# Tags: can be used for filtering projects.
tags = ["optimization-control", "model-predictive-control", "cryogenics", "thermodynamics"]

# Optional external URL for project (replaces project detail page).
external_link = ""

# Does the project detail page use math formatting?
math = false

# Optional featured image (relative to `static/img/` folder).
[header]
image = ""
caption = ""

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""

  # Show image only in page previews?
  preview_only = true

+++

Large cryogenic systems (e.g. cryoplant of the Large Hadron Collider), extract large heat loads at low temperature. This process requires much power at room temperature and cryogenic users and manufacturers have been for a long time aware of the importance of the energy efficiency of these devices. Indeed, these large cryoplants are optimized for a certain design point, and it has been possible in the past years to reach an efficiency of 20% of the Carnot efficiency in the LHC cryoplant. However, such large cryoplants are tricky to control, and subjected to some instabilities as soon as the heat loads change significantly above a certain time scale. Moreover, when heat loads change, the optimum efficiency, reached at the design point, is no longer guaranteed, as the optimum efficiency is the result of a complex compromise between the operations of different components. It would be of major interest for cryogenic users to have at their disposal a tool ensuring that the electrical consumption of the cryoplant will always be minimum. This is the objective of this project. In this project, we propose to develop a totally new control system for large refrigerators, which amazingly still use so far very simple PIDs, in spite of their complexity. Such a control system could also be used in any complex cryogenic system, where heat loads are not constant in time. Our approach is the following: first we will base our control system on a dynamic modeling of a large cryoplant. In the recent years, steady improvements were made in the dynamic modeling of such complex devices, and we will build upon recent results obtained at CERN and at CEA Grenoble. Based on such modeling, we will divide the refrigerator into different subsystems. Then the description of these subsystems will be based on “control oriented” simplified models, which will still describe accurately the subsystems, but will require much less memory and calculation than the general physics driven model of the refrigerator. This will enable an easier implementation of these simplified models in a PLC. Each subsystem will be controlled by its local controller, with various interactions with its neighbors. In this project, we plan to use a “Parametrized Distributed in Time Model Predictive Control” scheme, which seems the most promising local multivariable controller, and the most suited to our constrained environment. This new approach is a generalization of the MPC scheme, which is likely to enable an optimized control within a real time system such as a cryogenic refrigerator. The different subsystems will need to exchange information between each other, and some decisions will be needed, in order to solve possible conflicts. This is a typical case, where a cooperative control architecture would bring a major improvement. In this domain, GIPSA-lab has a prominent experience, and will therefore bring its skill in the definition of such an innovative architecture. Within this project, we therefore plan to develop a totally innovative control scheme of a cryogenic refrigerator. All the different steps will need to be carefully experimentally validated, and this will be done in the medium-sized cryogenic refrigerator available at CEA-SBT. This refrigerator is totally dedicated to R&D, and will be made available for verifying the models, testing local controllers, and evaluating the benefits brought by the innovative architecture developed within this project. A medium sized company will be in charge of the software translation to PLC, enabling an efficient and rapid development of the controller. Final tests, either on a simulator of a CERN refrigerator, or, if it is available, on a large cryogenic refrigerator itself based at CERN, will be performed to finally validate the whole development. This project needs an exceptional variety of prominent expertise(cryogenics,thermodynamic cycles, control systems and PLCs), which are gathered in the CRYOGREEN project submitted here.

## Cryogenic Plants at CEA and CERN

{{< gallery >}}

## Explicit Constrained Control of Warm Compression Stations

### Process configuration and dynamic simulator

[![Warm compression station configuration](wcs-config.png)](wcs-config.png)

[![Warm compression station](wcs-simulator.png)](wcs-simulator.png)

### Allocation control and validation results

[![Allocation control](wcs-allocation.png)](wcs-allocation.png)

[![Validation result](wcs-valid.png)](wcs-valid.png)

## Hierarchical Constrained Control of Cryogenic Refrigerators

### Process diagram and dynamic simulator

[![Process diagram](process-diagram.png)](process-diagram.png)

[![Brayton cycle](br-simulator.png)](br-simulator.png)

[![Joule-Thompson cycle](jt-simulator.png)](jt-simulator.png)

### Hierarchical control algorithm and numerical results

[![Hierarchical control algorithm](hdmpc-algo.png)](hdmpc-algo.png)

[![Convergence result](aa-convergence.png)](aa-convergence.png)

