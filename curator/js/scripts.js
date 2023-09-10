var BASE = "http://localhost:7789"
var APIKEY = "sk_nw4MHC0RIiDiqHWHhK2SKT4gnzs5iAUX-ALVQPq-y5rCWteDDCk14lYskdOrh5HwpcU"
var URL = `${BASE}/v1`
const WEBSOCKET = BASE;
var CHAINID = "64f8ca393f6603da0cb88da9"


class ProfileRecommendation {
    constructor(apiUrl, websocketUrl) {
        this.apiUrl = `${URL}/chain/run?chain_id=${CHAINID}`;
        this.socket = io.connect(WEBSOCKET);
        this.init();
    }

    init() {
        $('#button-search').on('click', () => {
            const userInput = $('#user-input').val();
            this.initSocket(userInput)
        });

        $('#user-input').on('keypress', (e) => {
            if (e.which === 13) { // Enter key code
                const userInput = $('#user-input').val();
                this.initSocket(userInput)
            }
        });
    }

    initSocket(userInput) {
        // Disable the button
        $('#button-search').prop('disabled', true);

        // Clear the results & streamed accordion
        $('#response-placeholder').empty();
        $('#streaming-placeholder').empty();

        $.ajax({
            url: `${URL}/stream`,
            method: 'GET',
            headers: {
                "Authorization": APIKEY
            },
            success: (data) => {
                this.runChain(userInput, data.stream_id)
                this.socket.on(data.stream_id, (data) => {
                    this.updateAccordion(data);
                })
            },
            error: (xhr, textStatus, errorThrown) => {
                console.error("Failed to initialize session:", errorThrown);
            }
        });
    }

    runChain(userInput, streamID) {
        $.ajax({
            url: `${this.apiUrl}&stream_id=${streamID}`,
            method: 'POST',
            headers: {
                "Authorization": APIKEY,
                "Content-Type": "application/json"
            },
            data: JSON.stringify({
                "request": { "query": userInput }
            }),
            beforeSend: () => {
                $('#loading').show();
            },
            complete: (data) => {
                $('#loading').hide();
                this.updateProfiles(data.responseJSON);
                $('#button-search').prop('disabled', false);
            }
        });
    }


    updateAccordion(data) {
        const placeholder = $('#streaming-placeholder');
        // clear
        // placeholder.html("");

        const objData = JSON.parse(data);

        // Create accordion item
        let accordionItem = `
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading${objData.stage_id}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${objData.stage_id}" aria-expanded="false" aria-controls="${objData.stage_id}">
                        <span>
                            stage_id: <span class="code">${objData.stage_id}</span> querying: <span class="code">${objData.type}</span>
                        </span>
                    </button>
                </h2>
                <div id="${objData.stage_id}" class="accordion-collapse collapse" aria-labelledby="heading${objData.stage_id}" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <pre><code>${JSON.stringify(objData, null, 4)}</code></pre>
                    </div>
                </div>
            </div>`;

        // Append to placeholder
        placeholder.append(accordionItem);
    }



    updateProfiles(data) {
        const placeholder = $('#response-placeholder');

        const finalResult = data[data.length - 1].profiles;

        finalResult.forEach(item => {
            let name = item.name;
            let explanation = item.explanation;
            let skills_list = item.skills_list;

            let badges = '';
            let colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'];
            skills_list.forEach((skill, index) => {
                let color = colors[index % colors.length];
                badges += `<span class="badge bg-${color} rounded-pill">${skill}</span> `;
            });

            let cardBody = `
                <div class="card mb-4">
                    <div class="card-body">
                        <h3 class="card-title">${name}</h3>
                        <p class="card-text">${explanation}</p>
                        <div class="center-vertically">
                            ${badges}
                        </div>
                    </div>
                </div>
                `;

            placeholder.append(cardBody);
        });

    }

}


class RenderPage {
    constructor() {
        this.init();
    }

    init() {
        // get chains
        $.ajax({
            url: `${URL}/chain?chain_id=${CHAINID}`,
            method: 'GET',
            headers: {
                "Authorization": APIKEY
            },
            complete: (data) => {
                let resp = data.responseJSON
                this.renderChains(resp.chain)
            }
        });

        // get sources
        $.ajax({
            url: `${URL}/source`,
            method: 'GET',
            headers: {
                "Authorization": APIKEY
            },
            complete: (data) => {
                let resp = data.responseJSON
                this.renderSources(resp)
            }
        });

    }
    renderChains(chain) {

        const placeholder = $('#chains-placeholder');

        chain.forEach((item) => {
            const stageId = item.stage_id;
            const queryType = item.type;
            const config = JSON.stringify(item.config, null, 4);

            const accordionItem = `
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingsidebar-${stageId}">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebar-${stageId}" aria-expanded="false" aria-controls="sidebar-${stageId}">
                            <span>
                                stage_id: <span class="code">${stageId}</span>
                            </span>
                        </button>
                    </h2>
                    <div id="sidebar-${stageId}" class="accordion-collapse collapse" aria-labelledby="headingsidebar-${stageId}" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <pre><code>${config}</code></pre>
                        </div>
                    </div>
                </div>`;

            placeholder.append(accordionItem);

        })
    }


    renderSources(sources) {

        const placeholder = $('#source-placeholder');

        sources.forEach((item) => {
            const sourceId = item.source_id;
            const type = item.type;
            const payload = JSON.stringify(item, null, 4);

            const accordionItem = `
                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading${sourceId}">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${sourceId}" aria-expanded="false" aria-controls="${sourceId}">
                            <span>
                                source_id: <span class="code">${sourceId}</span>
                            </span>
                        </button>
                    </h2>
                    <div id="${sourceId}" class="accordion-collapse collapse" aria-labelledby="heading${sourceId}" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <pre><code>${payload}</code></pre>
                        </div>
                    </div>
                </div>`;

            placeholder.append(accordionItem);

        })
    }

}

// Instantiate the class to make the API calls on page load
$(document).ready(() => {
    new RenderPage();
    new ProfileRecommendation();
});