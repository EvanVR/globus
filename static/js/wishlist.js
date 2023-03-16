function Wishlist() {
    // const GOATS_PER_PAGE = numRows * goatsPerRow;

    this.update = (data) => {
        const numOfRows = data.total;
        console.log(numOfRows);
        console.log(data.trips);
        $('thead tr').empty();
        const head_row = $(`
            <td>Image</td>
            <td>Name</td>
            <td>Price</td>
            <td>Book/Unbook</td>
        `);

        // $(head_row).find('.reset-btn').on('click', _ => {
        //     this.reset();
        // }); 

        $('thead tr').append(head_row);
        //////////////////////////////////////
        $('tbody').empty();

        for (let i = 0; i < numOfRows; i++) {
            const trip = data.trips[i];
            const row = $(`
                <tr id="${trip.id}" class="${trip.booked == -1? 'unbooked':''}">
                    <td><img class="img-fluid" src="/static/img/${trip.image}"></td>
                    <td>${trip.name}</td>
                    <td class="available">${trip.price}</td>
                    <td class="reset-col"><button class="minus">Unbook</button></td> 
                </tr>
            `);

            $(row).find('.minus').on('click', _ => {
                this.unbook(trip.id);
            });

            // $(row).find('.plus').on('click', _ => {
            //     this.increase(trip);
            // });

            $('tbody').append(row);
        }
    }

    this.load = () => {
        $.get('/api/my_trips', 
        (trips) => {
            this.update(trips);
        });
    }

   
    this.book = (id) => {
        console.log(id);
        $.post('/api/book_trip', {
            trip_id: id,
        }, (data) => {
            this.update(data);
        });
    }

    this.unbook = (id) => {
        $.post('/api/unbook_trip', {
            trip_id: id,
        }, (data) => {
            this.update(data);
        });
    }





    // this.updateCards = (goats) => {
    //     $('#cards').empty();

    //     for (let row = 0; row < numRows; row++) {
    //         const deck = $('<div class="card-deck"></div>');

    //         for (let col = 0; col < goatsPerRow; col++) {
    //             const index = row * goatsPerRow + col;
    //             if (index < goats.length) {
    //                 const goat = goats[row * goatsPerRow + col];

    //                 const card = $(`
    //                     <div class="card ${myGoats || goat.booked < 0 ? '' : 'booked'}">
    //                         <img class="card-img-top" src="/static/img/${goat.image}">
    //                         <div class="card-body">
    //                             <h5 class="card-title">${goat.name}</h5>
    //                             <p class="card-text">${goat.price} years old</p>
    //                             <button class="adopt-button btn btn-primary">
    //                                 ${myGoats ? 'Unbook' : 'Book'}
    //                             </button>
    //                         </div>
    //                     </div>
    //                 `);

    //                 $(card).find('.adopt-button').on('click', _ => {
    //                     if (myGoats)
    //                         this.unbook(goat);
    //                     else
    //                         this.book(goat);
    //                 });

    //                 $(deck).append(card);
    //             } else {

    //                 const card = $(`
    //                     <div class="card">
    //                     </div>
    //                 `);
    //                 $(deck).append(card);

    //             }
    //         }

    //         $('#cards').append(deck);
    //     }
    // }

    // const createPageLink = (text, toPage, active, disabled) => {
    //     const link = $(`
    //         <li class="page-item">
    //             <a class="page-link">${text}</a>
    //         </li>
    //     `);
    //     $(link).find('.page-link').on('click', _ => {
    //         this.currentPage = toPage;
    //         this.load();
    //     });
    //     if (active)
    //         link.addClass('active');
    //     if (disabled)
    //         link.addClass('disabled');
    //     return link;
    // }

    // this.currentPage = 1;

    // this.updatePagination = (total) => {
    //     let pages = Math.ceil(total / GOATS_PER_PAGE);
    //     $('#paginator').empty().append(
    //         createPageLink('Previous', this.currentPage - 1, false, this.currentPage == 1)
    //     );
    //     for (let page = 1; page <= pages; page++)
    //         $('#paginator').append(
    //             createPageLink(page, page, page == this.currentPage, false)
    //         );
    //     $('#paginator').append(
    //         createPageLink('Next', this.currentPage + 1, false, this.currentPage == pages)
    //     );
    // }

    // this.update = (data) => {
    //     this.updateCards(data.goats);
    //     this.updatePagination(data.total);
    // }

    // this.load = () => {
    //     $.get(myGoats ? '/api/my_goats' : '/api/get_goats', {
    //         n: GOATS_PER_PAGE,
    //         offset: (this.currentPage - 1) * GOATS_PER_PAGE
    //     }, (data) => {
    //         this.update(data);
    //     });
    // }

}
