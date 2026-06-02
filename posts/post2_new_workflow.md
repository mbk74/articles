# A new question

One question keeps coming back to me:

If AI can dynamically change the number of screens in a workflow, should ViewModels still belong to screens?

In a traditional booking flow we might have:

SearchViewModel
ResultsViewModel
CheckoutViewModel

But if tomorrow the same task takes two screens instead of five, this separation starts to feel artificial.

Maybe the ViewModel of the future represents a task rather than a screen.

The booking process stays the same.

Only the presentation changes.

Has anyone experimented with something similar in production?

#AI #iOS #Android #MVVM #SwiftUI #JetpackCompose #SoftwareArchitecture #MobileDevelopment
