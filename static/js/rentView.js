// Danai Roumelioti, dr3248@drexel.edu
// CS530: dr3248, Assignment 2 

function rentView() {

    this.update = (bikes) => {
        const numOfRows = bikes.length;

        $('thead tr').empty();
        const head_row = $(`
            <td>Image</td>
            <td>Name</td>
            <td>Available</td>
            <td class="reset-col"><button class="reset-btn">Reset</button></td>
        `);

        $(head_row).find('.reset-btn').on('click', _ => {
            this.reset();
        }); 

        $('thead tr').append(head_row);
        //////////////////////////////////////
        $('tbody').empty();

        for (let i = 0; i < numOfRows; i++) {
            const bike = bikes[i];
            const row = $(`
                <tr id="${bike.id}" class="${bike.available == 0? 'unavailable':''}">
                    <td><img class="img-fluid" src="/static/img/bikes/${bike.image}"></td>
                    <td>${bike.name}</td>
                    <td class="available">${bike.available}</td>
                    <td class="reset-col"><button class="quantity-btn minus">-</button><button class="quantity-btn plus">+</button></td> 
                </tr>
            `);

            $(row).find('.minus').on('click', _ => {
                this.decrease(bike);
            });

            $(row).find('.plus').on('click', _ => {
                this.increase(bike);
            });

            $('tbody').append(row);
        }
    }

    this.load = () => {
        $.get('/api/get_bikes', 
        (bikes) => {
            this.update(bikes);
        });
    }

    this.decrease = (bike) => {
        if(bike.available > 0) {
            $.post('/api/update_bike', {
                id: bike.id,
                available: (bike.available - 1),
            }, (bikes) => {
                this.update(bikes);
            });

            //animate press
            $("#" + bike.id + " button.minus").last().addClass("pressed");
            setTimeout(function () {
                $("#" + bike.id + " button.minus").last().removeClass("pressed");
            }, 100);
        
            //retrieve current availability
            available = $("#" + bike.id + " .available").first().text();
        
            if(available === 0) {
                $("#" + bike.id).last().toggleClass("unavailable");
            }
        }
    }

    this.increase = (bike) => {
        $.post('/api/update_bike', {
            id: bike.id,
            available: (bike.available + 1),
        }, (bikes) => {
            this.update(bikes);
        });

        //animate press
        $("#" + bike.id + " button.plus").last().addClass("pressed");
        setTimeout(function () {
            $("#" + bike.id + " button.plus").last().removeClass("pressed");
        }, 100);
        
        //retrieve current availability
        available = $("#" + bike.id + " .available").first().text();

        //in case line was grayed out
        if(available == 1) {
            $("#" + bike.id).last().toggleClass("unavailable");
        }
    }


    this.reset = () => {
        $.post('/api/reset_bikes', {
            available: 3,
        }, (bikes) => {
            this.update(bikes);
        });
   
        // animate press
        $(".reset-btn").last().addClass("pressed");
        setTimeout(function () {
            $(".reset-btn").last().removeClass("pressed");
        }, 100);

        var numOfRows = $(".table tr").length;
        for(var i = 1; i < numOfRows; i++) {
            $("#b" + i).last().removeClass("unavailable");
        }
    }

}