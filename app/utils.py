import plotly
import plotly.graph_objs as go
import json
import re

# The following method reutrns a histogram of list passed in JSON form.
def plot_lenght_distribution(samples):

    # Initializing plotly figure
    fig = go.Figure()

    # Appeding all samples
    for sample_name,sample in samples.items():

        len_data = sample.getCombniedData()['Length']

        fig.add_trace(go.Histogram(
                            x=len_data,
                            histnorm = 'percent',
                            name = sample_name,
                            error_y=dict( 
                                type='data', 
                                array=sample.getPeptideLengthError()/2, 
                                color='green', 
                                thickness=1, 
                                width=5, 
                            )
                        )
        )

    # Adding labels in the chart
    fig.update_layout(
            title='The frequency distribution of the peptide lengths',
            xaxis = dict(title='<i>Length</i>'),
            yaxis = dict(title='<i>% Peptides</i>')
        )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

    
# The following method filters the data to remove contamination.
# This method is specific to a PEAKS output file for peptides.
def filterPeaksFile(samples, dropPTM=True, minLen=1, maxLen=133):
    
    for file_name,sample in samples.items():
#       Removing rows with no accession identity
        samples[file_name] = sample.dropna(subset=['Accession'])
        
#       Dropping the peptides with Post translational modifications
        if dropPTM:
            samples[file_name] = sample[sample.apply(lambda x : re.search(r'[(].+[)]',x['Peptide']) == None,axis=1)]

#       Removing contamincation founf from accession number 
        samples[file_name] = sample[sample.apply(lambda x : str(x['Accession']).find('CONTAM') == -1,axis=1)]
        
#       Filtering on the basis of the peptide length
        samples[file_name] = sample[sample.apply(lambda x : x['Length'] in range(minLen,maxLen),axis=1)]
    
    return samples