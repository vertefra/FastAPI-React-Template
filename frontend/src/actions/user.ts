import { User } from '../interfaces/User';
import axios, { AxiosPromise, AxiosRequestConfig, AxiosResponse } from 'axios';
import { baseURL } from '../settings';

export const login = async (user: User): Promise<User> => {
	try {
		const { data } = await axios.post(`${baseURL}/users/login`, user);
		return data;
	} catch (err) {
		return err;
	}
};

export const signup = async (user: User): Promise<User> => {
	try {
		const { data } = await axios.post(`${baseURL}/users/signup`, user);
		return data;
	} catch (err) {
		return err;
	}
};
