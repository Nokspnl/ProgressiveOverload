# CQF Progessive Overload #

## The Motivation and the Idea ##
* Input data related to your current gym session directly in your phone
* Store the data in an SQL Library
* Develop an algorithm based on the given data which predicts your output in the next session 
* Learn based on the residuals i.e. predicted vs. actual data

### The Algorithm ###
I aim to determine the optimal weight and repetition goal given an information set I. 
In mathematical terms, we simply aim to compute:

$$ E(Output | Information)  $$

Then compute the residuals as:

$$ u = y - E(Output | Information) $$

And feed the algorithm to minimize these residuals over time. 

We naturally must define the information set. I expect this to be related somehow to the following:
* The output at t-1, t-2, (...) t-k
* The amount of sleep, food, fluids, caffeine (...) you have gotten on the day of the session.
* A qualitative "feeling" of well being on the day of the session

We must assume that the user delivers correct measures for the two latter points in order to minimise the residuals.

I will initially assume a (pretty lazy) setup. The minimum amount of reps is 8, maximum is 15. 
Therefore, as soon as any lift reaches 15 reps, the algorithm should automatically adjust the weight. 
On the contrary, if the output at t-1 was 30kg at 13 reps, the algorithm will favour suggesting an increased amount 
of reps rather than weight. 

### A ###