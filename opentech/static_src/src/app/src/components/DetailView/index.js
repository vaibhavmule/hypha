import React, { Component } from 'react'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { withWindowSizeListener } from 'react-window-size-listener';

import DisplayPanel from '@containers/DisplayPanel';
import SlideInRight from '@components/Transitions/SlideInRight'
import SlideOutLeft from '@components/Transitions/SlideOutLeft'
import { getCurrentSubmissionID } from '@selectors/submissions';

import './style.scss';

class DetailView extends Component {

    isMobile = (width) => (width ? width : this.props.windowSize.windowWidth) < 1024

    renderDisplay () {
        return <DisplayPanel />
    }

    render() {
        const { listing, submission } = this.props;

        const activeSubmission = !!submission;

        if (this.isMobile()) {
            var activeDisplay;
            if (activeSubmission){
                activeDisplay = (
                    <SlideInRight key={"display"}>
                        { this.renderDisplay }
                    </SlideInRight>
                )
            } else {
                activeDisplay = (
                    <SlideOutLeft key={"listing"}>
                        {listing}
                    </SlideOutLeft>
                )
            }

            return (
                <div className="detail-view">
                    { activeDisplay }
                </div>
            )
        } else {
            return (
                <div className="detail-view">
                    {listing}
                    { this.renderDisplay }
                </div>
            )
        }

    }
};

DetailView.propTypes = {
    listing: PropTypes.node.isRequired,
    hasActiveApplication: PropTypes.bool,
};

const mapStateToProps = state => ({
    submission: getCurrentSubmissionID(state),
});

const mapDispatchToProps = dispatch => ({
    loadSubmission: id => dispatch(fetchSubmission(id)),
    clearCurrentSubmission: () => dispatch(clearCurrentSubmission()),
});

export default connect(mapStateToProps)(withWindowSizeListener(DetailView));
