# SECMizzouCyberChallenge

Currently, in our healthcare infrastructure today, there are several security issues that deep moats and high walls can’t fix. No matter how secure you make your firewall to the outside world, a malicious actor on the inside that is allowed access could compromise your data. If an organization is secured, only the individuals who have HIPPA training are authorized to have access to the Protected Health Information (PHI). However, according to hippajournal.com, “the healthcare industry is unique as the biggest security threat comes from within. Insiders were responsible for almost 58% of all breaches with external actors confirmed as responsible for just 42% of incidents.” This is significant, as the other 42% includes several different other types of breach methods, such as theft, loss, and improper disposal. The issue comes from a lack of an ability to detect insider breaches in real time, since a significant amount of breaches are not detected for months, if not years, after they occur. A large issue with this is that the attacker can remain on the system for quite some time after the initial breach.

Real world examples are in the powerpoint. 

The current model that exists is designed to protect attacks from the outside extremely well, but sometimes neglects to mitigate internal attacks.

Therefore, we have designed a method that is proactive against these internal attacks instead of reactive. We have implemented a proactive solution that uses verification, authorization, and consent methods to mitigate attack vectors. Our solution does this by identifying anomalous changes in the system by trusted users and provides access control to give multi-party consent to a task such as a data value change. This access control will be weighted by the risk associated with changing the data and the risk associated with releasing the data. 

Future ideas:

AD integration

